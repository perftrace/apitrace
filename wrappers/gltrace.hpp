/**************************************************************************
 *
 * Copyright 2011 Jose Fonseca
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 **************************************************************************/

#ifndef _GLTRACE_HPP_
#define _GLTRACE_HPP_


#include <string.h>
#include <stdlib.h>
#include <map>
#include <list>
#include "glimports.hpp"
#include "glsize.hpp"

namespace gltrace {


enum Profile {
    PROFILE_COMPAT,
    PROFILE_ES1,
    PROFILE_ES2,
};


/**
 * OpenGL ES buffers cannot be read. This class is used to track index buffer
 * contents.
 */
class Buffer {
public:
    GLsizeiptr size;
    GLvoid *data;

    Buffer() :
        size(0),
        data(0)
    {}

    ~Buffer() {
        free(data);
    }

    void
    bufferData(GLsizeiptr new_size, const void *new_data) {
        if (new_size < 0) {
            new_size = 0;
        }
        size = new_size;
        data = realloc(data, new_size);
        if (new_size && new_data) {
            memcpy(data, new_data, size);
        }
    }

    void
    bufferSubData(GLsizeiptr offset, GLsizeiptr length, const void *new_data) {
        if (offset >= 0 && offset < size && length > 0 && offset + length <= size && new_data) {
            memcpy((GLubyte *)data + offset, new_data, length);
        }
    }

    void
    getSubData(GLsizeiptr offset, GLsizeiptr length, void *out_data) {
        if (offset >= 0 && offset < size && length > 0 && offset + length <= size && out_data) {
            memcpy(out_data, (GLubyte *)data + offset, length);
        }
    }
};

struct TextureLevel
{
    GLint level;
    GLsizei width;
    GLsizei height;
    GLsizei depth;
    GLsizei imageSize;
};

// this helps track texture parameters that are needed to recreate a texture
class Texture {
public:
    GLenum name;
    GLenum target;
    GLint internalFormat;
    GLenum format;
    GLenum type;

    // list of mipmap levels that had contents uploaded
    std::list<TextureLevel> levels;

    Texture() :
       name(GL_NONE),
       target(GL_NONE),
       format(GL_NONE),
       type(GL_NONE)
    {}

    ~Texture() {
    }

    void texImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLenum format, GLenum type)
    {
        SetTextureInfo(name, target, internalFormat, format, type);
        GLsizei imageSize = (GLsizei)_gl_image_size(format, type, width, 1, 1, true); //_glTexImage1D_size(format, type, width);
        AddTextureLevel(level, width, 1, 1, imageSize);
    }

    void texImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLenum format, GLenum type)
    {
        SetTextureInfo(name, target, internalFormat, format, type);
        GLsizei imageSize = (GLsizei)_gl_image_size(format, type, width, height, 1, true); //_glTexImage2D_size(format, type, width, height);
        AddTextureLevel(level, width, height, 1, imageSize);
    }

    void texImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type)
    {
        SetTextureInfo(name, target, internalFormat, format, type);
        GLsizei imageSize = (GLsizei)_gl_image_size(format, type, width, height, depth, true); //_glTexImage3D_size(format, type, width, height, depth);
        AddTextureLevel(level, width, height, depth, imageSize);
    }

    void compressedTexImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei imageSize)
    {
        SetTextureInfo(name, target, internalFormat, format, GL_NONE);
        AddTextureLevel(level, width, 1, 1, imageSize);
    }

    void compressedTexImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei imageSize)
    {
        SetTextureInfo(name, target, internalFormat, format, GL_NONE);
        AddTextureLevel(level, width, height, 1, imageSize);
    }

    void compressedTexImage(GLuint name, GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLsizei imageSize)
    {
        SetTextureInfo(name, target, internalFormat, format, GL_NONE);
        AddTextureLevel(level, width, height, depth, imageSize);
    }

private:
    void SetTextureInfo(GLuint name, GLenum target, GLint internalFormat, GLenum format, GLenum type)
    {
        if (this->name == 0)
        {
            // we only want to populate this information the first time
            this->name = name;
            this->target = target;
            this->internalFormat = internalFormat;
            this->format = format;
            this->type = type;
        }
    }

    void AddTextureLevel(GLint level, GLsizei width, GLsizei height, GLsizei depth, GLsizei compressedImageSize)
    {
        // see if the layer is already in the list
        std::list<gltrace::TextureLevel>::iterator iter = this->levels.begin();
        for (; iter != this->levels.end(); ++iter)
        {
            if (iter->level == level)
            {
                // level already exists
                break;
            }
        }

        if (iter != this->levels.end())
        {
            // update the level
            iter->width = width;
            iter->height = height;
            iter->depth = depth;
            iter->imageSize = compressedImageSize;
        }
        else
        {
            TextureLevel texLevel;
            texLevel.level = level;
            texLevel.width = width;
            texLevel.height = height;
            texLevel.depth = depth;
            texLevel.imageSize = compressedImageSize;
            this->levels.push_back(texLevel);
        }
    }
};

class Shader {
public:
    GLsizei count;
    GLchar** sources;
    GLsizei* lengths;
    GLenum type;

    Shader()
        : sources(NULL),
        lengths(NULL),
        count(0),
        type(GL_NONE)
    {
    }

    ~Shader()
    {
        Cleanup();
    }

    void SetSources(GLenum type, GLsizei n, const GLchar* const * shaderSources, GLsizei* shaderLengths)
    {
        Cleanup();

        this->type = type;
        count = n;

        if (count > 0) {
            sources = new (std::nothrow) GLchar*[count];
            lengths = new (std::nothrow) GLsizei[count];

            if (sources != NULL && lengths != NULL) {
                for (GLsizei i = 0; i < n; ++i) {
                    GLsizei length = 0;
                    if (shaderLengths != NULL) {
                        length = shaderLengths[i];
                    } else {
                        length = (GLsizei)strlen(shaderSources[i]) + 1;
                    }

                    sources[i] = new (std::nothrow) GLchar[length];
                    if (sources[i] != NULL)
                    {
                        memcpy(sources[i], shaderSources[i], length*sizeof(GLchar));
                        sources[i][length-1] = '\0';
                        lengths[i] = length;
                    }
                }
            }
            else
            {
                assert(!"Out of memory when attempting to allocate memory for shader sources.");
                Cleanup();
            }
        }
    }

private:
    void Cleanup()
    {
        if (sources != NULL)
        {
            for (GLsizei i = 0; i < count; ++i) {
                delete [] sources[i];
                sources[i] = NULL;
            }

            delete [] sources;
            sources = NULL;
        }

        if (lengths != NULL)
        {
            delete [] lengths;
            lengths = NULL;
        }

        count = 0;
        type = GL_NONE;
    }
};

class Program {
public:
    bool linked;

    std::map<GLuint, Shader> shaders;

    void AddShader(GLuint shaderName, GLenum shaderType, const GLchar* shaderSource, GLsizei shaderLength)
    {
        if (shaderSource != NULL) {
            shaders[shaderName].SetSources(shaderType, 1, &shaderSource, &shaderLength);
        }
    }

    Program()
        : linked(false)
    {
    }

    ~Program()
    {
        shaders.clear();
    }
};

class Context {
public:
    enum Profile profile;
    bool user_arrays;
    bool user_arrays_arb;
    bool user_arrays_nv;
    unsigned retain_count;
    uintptr_t hdc;

    // TODO: This will fail for buffers shared by multiple contexts.
    std::map <GLuint, Buffer> buffers;

    // Used by state snapshot
    std::map<GLuint, Texture> textures;
    std::map<GLuint, Program> programs;
    std::list<GLuint> pipelines;
    std::map<GLuint, Shader> separateShaders;
    std::list<GLuint> framebuffers;
    std::list<GLuint> vertexArrays;
    std::list<GLuint> bufferObjects;
    std::list<GLuint> samplers;
    std::list<GLuint> renderbuffers;

    Context(void) :
        profile(PROFILE_COMPAT),
        user_arrays(false),
        user_arrays_arb(false),
        user_arrays_nv(false),
        retain_count(0),
        hdc(NULL)
    { }

    ~Context(void)
    {
        buffers.clear();
        textures.clear();
        programs.clear();
        pipelines.clear();
        separateShaders.clear();
        framebuffers.clear();
        vertexArrays.clear();
        bufferObjects.clear();
        samplers.clear();
        renderbuffers.clear();
    }

    inline bool
    needsShadowBuffers(void)
    {
        return profile == PROFILE_ES1 || profile == PROFILE_ES2;
    }
};

void
createContext(uintptr_t hdc, uintptr_t context_id);

void
retainContext(uintptr_t context_id);

bool
releaseContext(uintptr_t context_id);

void
setContext(uintptr_t context_id);

void
clearContext(void);

gltrace::Context *
getContext(void);

const GLubyte *
_glGetString_override(GLenum name);

void
_glGetIntegerv_override(GLenum pname, GLint *params);

const GLubyte *
_glGetStringi_override(GLenum name, GLuint index);


} /* namespace gltrace */


#endif /* _GLRETRACE_HPP_ */
