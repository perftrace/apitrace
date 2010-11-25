##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3d9types.h"""

from winapi import *

D3DCOLOR = Alias("D3DCOLOR", DWORD)

D3DVECTOR = Struct("D3DVECTOR", [
    (Float, "x"),
    (Float, "y"),
    (Float, "z"),
])

D3DCOLORVALUE = Struct("D3DCOLORVALUE", [
    (Float, "r"),
    (Float, "g"),
    (Float, "b"),
    (Float, "a"),
])

D3DRECT = Struct("D3DRECT", [
    (LONG, "x1"),
    (LONG, "y1"),
    (LONG, "x2"),
    (LONG, "y2"),
])

D3DMATRIX = Struct("D3DMATRIX", [
    (Array(Array(Float, "4"), "4"), "m"),
])

D3DVIEWPORT9 = Struct("D3DVIEWPORT9", [
    (DWORD, "X"),
    (DWORD, "Y"),
    (DWORD, "Width"),
    (DWORD, "Height"),
    (Float, "MinZ"),
    (Float, "MaxZ"),
])

D3DCLIP = Flags(DWORD, [
    "D3DCLIPPLANE0",
    "D3DCLIPPLANE1",
    "D3DCLIPPLANE2",
    "D3DCLIPPLANE3",
    "D3DCLIPPLANE4",
    "D3DCLIPPLANE5",
])

D3DCS = Flags(DWORD, [
    "D3DCS_ALL",
    "D3DCS_LEFT",
    "D3DCS_RIGHT",
    "D3DCS_TOP",
    "D3DCS_BOTTOM",
    "D3DCS_FRONT",
    "D3DCS_BACK",
    "D3DCS_PLANE0",
    "D3DCS_PLANE1",
    "D3DCS_PLANE2",
    "D3DCS_PLANE3",
    "D3DCS_PLANE4",
    "D3DCS_PLANE5",
])

D3DCLIPSTATUS9 = Struct("D3DCLIPSTATUS9", [
    (DWORD, "ClipUnion"),
    (DWORD, "ClipIntersection"),
])

D3DMATERIAL9 = Struct("D3DMATERIAL9", [
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Emissive"),
    (Float, "Power"),
])

D3DLIGHTTYPE = Enum("D3DLIGHTTYPE", [
    "D3DLIGHT_POINT",
    "D3DLIGHT_SPOT",
    "D3DLIGHT_DIRECTIONAL",
    "D3DLIGHT_FORCE_DWORD",
])

D3DLIGHT9 = Struct("D3DLIGHT9", [
    (D3DLIGHTTYPE, "Type"),
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DVECTOR, "Position"),
    (D3DVECTOR, "Direction"),
    (Float, "Range"),
    (Float, "Falloff"),
    (Float, "Attenuation0"),
    (Float, "Attenuation1"),
    (Float, "Attenuation2"),
    (Float, "Theta"),
    (Float, "Phi"),
])

D3DCS = Flags(DWORD, [
    "D3DCLEAR_TARGET",
    "D3DCLEAR_ZBUFFER",
    "D3DCLEAR_STENCIL",
])

D3DSHADEMODE = Enum("D3DSHADEMODE", [
    "D3DSHADE_FLAT",
    "D3DSHADE_GOURAUD",
    "D3DSHADE_PHONG",
    "D3DSHADE_FORCE_DWORD",
])

D3DFILLMODE = Enum("D3DFILLMODE", [
    "D3DFILL_POINT",
    "D3DFILL_WIREFRAME",
    "D3DFILL_SOLID",
    "D3DFILL_FORCE_DWORD",
])

D3DBLEND = Enum("D3DBLEND", [
    "D3DBLEND_ZERO",
    "D3DBLEND_ONE",
    "D3DBLEND_SRCCOLOR",
    "D3DBLEND_INVSRCCOLOR",
    "D3DBLEND_SRCALPHA",
    "D3DBLEND_INVSRCALPHA",
    "D3DBLEND_DESTALPHA",
    "D3DBLEND_INVDESTALPHA",
    "D3DBLEND_DESTCOLOR",
    "D3DBLEND_INVDESTCOLOR",
    "D3DBLEND_SRCALPHASAT",
    "D3DBLEND_BOTHSRCALPHA",
    "D3DBLEND_BOTHINVSRCALPHA",
    "D3DBLEND_BLENDFACTOR",
    "D3DBLEND_INVBLENDFACTOR",
    "D3DBLEND_SRCCOLOR2",
    "D3DBLEND_INVSRCCOLOR2",
    "D3DBLEND_FORCE_DWORD",
])

D3DBLENDOP = Enum("D3DBLENDOP", [
    "D3DBLENDOP_ADD",
    "D3DBLENDOP_SUBTRACT",
    "D3DBLENDOP_REVSUBTRACT",
    "D3DBLENDOP_MIN",
    "D3DBLENDOP_MAX",
    "D3DBLENDOP_FORCE_DWORD",
])

D3DTEXTUREADDRESS = Enum("D3DTEXTUREADDRESS", [
    "D3DTADDRESS_WRAP",
    "D3DTADDRESS_MIRROR",
    "D3DTADDRESS_CLAMP",
    "D3DTADDRESS_BORDER",
    "D3DTADDRESS_MIRRORONCE",
    "D3DTADDRESS_FORCE_DWORD",
])

D3DCULL = Enum("D3DCULL", [
    "D3DCULL_NONE",
    "D3DCULL_CW",
    "D3DCULL_CCW",
    "D3DCULL_FORCE_DWORD",
])

D3DCMPFUNC = Enum("D3DCMPFUNC", [
    "D3DCMP_NEVER",
    "D3DCMP_LESS",
    "D3DCMP_EQUAL",
    "D3DCMP_LESSEQUAL",
    "D3DCMP_GREATER",
    "D3DCMP_NOTEQUAL",
    "D3DCMP_GREATEREQUAL",
    "D3DCMP_ALWAYS",
    "D3DCMP_FORCE_DWORD",
])

D3DSTENCILOP = Enum("D3DSTENCILOP", [
    "D3DSTENCILOP_KEEP",
    "D3DSTENCILOP_ZERO",
    "D3DSTENCILOP_REPLACE",
    "D3DSTENCILOP_INCRSAT",
    "D3DSTENCILOP_DECRSAT",
    "D3DSTENCILOP_INVERT",
    "D3DSTENCILOP_INCR",
    "D3DSTENCILOP_DECR",
    "D3DSTENCILOP_FORCE_DWORD",
])

D3DFOGMODE = Enum("D3DFOGMODE", [
    "D3DFOG_NONE",
    "D3DFOG_EXP",
    "D3DFOG_EXP2",
    "D3DFOG_LINEAR",
    "D3DFOG_FORCE_DWORD",
])

D3DZBUFFERTYPE = Enum("D3DZBUFFERTYPE", [
    "D3DZB_FALSE",
    "D3DZB_TRUE",
    "D3DZB_USEW",
    "D3DZB_FORCE_DWORD",
])

D3DPRIMITIVETYPE = Enum("D3DPRIMITIVETYPE", [
    "D3DPT_POINTLIST",
    "D3DPT_LINELIST",
    "D3DPT_LINESTRIP",
    "D3DPT_TRIANGLELIST",
    "D3DPT_TRIANGLESTRIP",
    "D3DPT_TRIANGLEFAN",
    "D3DPT_FORCE_DWORD",
])

D3DTRANSFORMSTATETYPE = Enum("D3DTRANSFORMSTATETYPE", [
    "D3DTS_VIEW",
    "D3DTS_PROJECTION",
    "D3DTS_TEXTURE0",
    "D3DTS_TEXTURE1",
    "D3DTS_TEXTURE2",
    "D3DTS_TEXTURE3",
    "D3DTS_TEXTURE4",
    "D3DTS_TEXTURE5",
    "D3DTS_TEXTURE6",
    "D3DTS_TEXTURE7",
    "D3DTS_FORCE_DWORD",
])

D3DTS = Flags(DWORD, [
    "D3DTS_WORLD",
    "D3DTS_WORLD1",
    "D3DTS_WORLD2",
    "D3DTS_WORLD3",
])

D3DRENDERSTATETYPE = Enum("D3DRENDERSTATETYPE", [
    "D3DRS_ZENABLE",
    "D3DRS_FILLMODE",
    "D3DRS_SHADEMODE",
    "D3DRS_ZWRITEENABLE",
    "D3DRS_ALPHATESTENABLE",
    "D3DRS_LASTPIXEL",
    "D3DRS_SRCBLEND",
    "D3DRS_DESTBLEND",
    "D3DRS_CULLMODE",
    "D3DRS_ZFUNC",
    "D3DRS_ALPHAREF",
    "D3DRS_ALPHAFUNC",
    "D3DRS_DITHERENABLE",
    "D3DRS_ALPHABLENDENABLE",
    "D3DRS_FOGENABLE",
    "D3DRS_SPECULARENABLE",
    "D3DRS_FOGCOLOR",
    "D3DRS_FOGTABLEMODE",
    "D3DRS_FOGSTART",
    "D3DRS_FOGEND",
    "D3DRS_FOGDENSITY",
    "D3DRS_RANGEFOGENABLE",
    "D3DRS_STENCILENABLE",
    "D3DRS_STENCILFAIL",
    "D3DRS_STENCILZFAIL",
    "D3DRS_STENCILPASS",
    "D3DRS_STENCILFUNC",
    "D3DRS_STENCILREF",
    "D3DRS_STENCILMASK",
    "D3DRS_STENCILWRITEMASK",
    "D3DRS_TEXTUREFACTOR",
    "D3DRS_WRAP0",
    "D3DRS_WRAP1",
    "D3DRS_WRAP2",
    "D3DRS_WRAP3",
    "D3DRS_WRAP4",
    "D3DRS_WRAP5",
    "D3DRS_WRAP6",
    "D3DRS_WRAP7",
    "D3DRS_CLIPPING",
    "D3DRS_LIGHTING",
    "D3DRS_AMBIENT",
    "D3DRS_FOGVERTEXMODE",
    "D3DRS_COLORVERTEX",
    "D3DRS_LOCALVIEWER",
    "D3DRS_NORMALIZENORMALS",
    "D3DRS_DIFFUSEMATERIALSOURCE",
    "D3DRS_SPECULARMATERIALSOURCE",
    "D3DRS_AMBIENTMATERIALSOURCE",
    "D3DRS_EMISSIVEMATERIALSOURCE",
    "D3DRS_VERTEXBLEND",
    "D3DRS_CLIPPLANEENABLE",
    "D3DRS_POINTSIZE",
    "D3DRS_POINTSIZE_MIN",
    "D3DRS_POINTSPRITEENABLE",
    "D3DRS_POINTSCALEENABLE",
    "D3DRS_POINTSCALE_A",
    "D3DRS_POINTSCALE_B",
    "D3DRS_POINTSCALE_C",
    "D3DRS_MULTISAMPLEANTIALIAS",
    "D3DRS_MULTISAMPLEMASK",
    "D3DRS_PATCHEDGESTYLE",
    "D3DRS_DEBUGMONITORTOKEN",
    "D3DRS_POINTSIZE_MAX",
    "D3DRS_INDEXEDVERTEXBLENDENABLE",
    "D3DRS_COLORWRITEENABLE",
    "D3DRS_TWEENFACTOR",
    "D3DRS_BLENDOP",
    "D3DRS_POSITIONDEGREE",
    "D3DRS_NORMALDEGREE",
    "D3DRS_SCISSORTESTENABLE",
    "D3DRS_SLOPESCALEDEPTHBIAS",
    "D3DRS_ANTIALIASEDLINEENABLE",
    "D3DRS_MINTESSELLATIONLEVEL",
    "D3DRS_MAXTESSELLATIONLEVEL",
    "D3DRS_ADAPTIVETESS_X",
    "D3DRS_ADAPTIVETESS_Y",
    "D3DRS_ADAPTIVETESS_Z",
    "D3DRS_ADAPTIVETESS_W",
    "D3DRS_ENABLEADAPTIVETESSELLATION",
    "D3DRS_TWOSIDEDSTENCILMODE",
    "D3DRS_CCW_STENCILFAIL",
    "D3DRS_CCW_STENCILZFAIL",
    "D3DRS_CCW_STENCILPASS",
    "D3DRS_CCW_STENCILFUNC",
    "D3DRS_COLORWRITEENABLE1",
    "D3DRS_COLORWRITEENABLE2",
    "D3DRS_COLORWRITEENABLE3",
    "D3DRS_BLENDFACTOR",
    "D3DRS_SRGBWRITEENABLE",
    "D3DRS_DEPTHBIAS",
    "D3DRS_WRAP8",
    "D3DRS_WRAP9",
    "D3DRS_WRAP10",
    "D3DRS_WRAP11",
    "D3DRS_WRAP12",
    "D3DRS_WRAP13",
    "D3DRS_WRAP14",
    "D3DRS_WRAP15",
    "D3DRS_SEPARATEALPHABLENDENABLE",
    "D3DRS_SRCBLENDALPHA",
    "D3DRS_DESTBLENDALPHA",
    "D3DRS_BLENDOPALPHA",
    "D3DRS_FORCE_DWORD",
])

D3DMATERIALCOLORSOURCE = Enum("D3DMATERIALCOLORSOURCE", [
    "D3DMCS_MATERIAL",
    "D3DMCS_COLOR1",
    "D3DMCS_COLOR2",
    "D3DMCS_FORCE_DWORD",
])

D3DWRAP = Flags(DWORD, [
    "D3DWRAP_U",
    "D3DWRAP_V",
    "D3DWRAP_W",
])

D3DWRAPCOORD = Flags(DWORD, [
    "D3DWRAPCOORD_0",
    "D3DWRAPCOORD_1",
    "D3DWRAPCOORD_2",
    "D3DWRAPCOORD_3",
])

D3DCOLORWRITEENABLE = Flags(DWORD, [
    "D3DCOLORWRITEENABLE_RED",
    "D3DCOLORWRITEENABLE_GREEN",
    "D3DCOLORWRITEENABLE_BLUE",
    "D3DCOLORWRITEENABLE_ALPHA",
])

D3DTEXTURESTAGESTATETYPE = Enum("D3DTEXTURESTAGESTATETYPE", [
    "D3DTSS_COLOROP",
    "D3DTSS_COLORARG1",
    "D3DTSS_COLORARG2",
    "D3DTSS_ALPHAOP",
    "D3DTSS_ALPHAARG1",
    "D3DTSS_ALPHAARG2",
    "D3DTSS_BUMPENVMAT00",
    "D3DTSS_BUMPENVMAT01",
    "D3DTSS_BUMPENVMAT10",
    "D3DTSS_BUMPENVMAT11",
    "D3DTSS_TEXCOORDINDEX",
    "D3DTSS_BUMPENVLSCALE",
    "D3DTSS_BUMPENVLOFFSET",
    "D3DTSS_TEXTURETRANSFORMFLAGS",
    "D3DTSS_COLORARG0",
    "D3DTSS_ALPHAARG0",
    "D3DTSS_RESULTARG",
    "D3DTSS_CONSTANT",
    "D3DTSS_FORCE_DWORD",
])

D3DSAMPLERSTATETYPE = Enum("D3DSAMPLERSTATETYPE", [

    "D3DSAMP_ADDRESSU",
    "D3DSAMP_ADDRESSV",
    "D3DSAMP_ADDRESSW",
    "D3DSAMP_BORDERCOLOR",
    "D3DSAMP_MAGFILTER",
    "D3DSAMP_MINFILTER",
    "D3DSAMP_MIPFILTER",
    "D3DSAMP_MIPMAPLODBIAS",
    "D3DSAMP_MAXMIPLEVEL",
    "D3DSAMP_MAXANISOTROPY",
    "D3DSAMP_SRGBTEXTURE",
    "D3DSAMP_ELEMENTINDEX",
    "D3DSAMP_DMAPOFFSET",
    "D3DSAMP_FORCE_DWORD",
])

D3DTSS = Flags(DWORD, [
    "D3DTSS_TCI_PASSTHRU",
    "D3DTSS_TCI_CAMERASPACENORMAL",
    "D3DTSS_TCI_CAMERASPACEPOSITION",
    "D3DTSS_TCI_CAMERASPACEREFLECTIONVECTOR",
    "D3DTSS_TCI_SPHEREMAP",
])

D3DTEXTUREOP = Enum("D3DTEXTUREOP", [
    "D3DTOP_DISABLE",
    "D3DTOP_SELECTARG1",
    "D3DTOP_SELECTARG2",
    "D3DTOP_MODULATE",
    "D3DTOP_MODULATE2X",
    "D3DTOP_MODULATE4X",
    "D3DTOP_ADD",
    "D3DTOP_ADDSIGNED",
    "D3DTOP_ADDSIGNED2X",
    "D3DTOP_SUBTRACT",
    "D3DTOP_ADDSMOOTH",
    "D3DTOP_BLENDDIFFUSEALPHA",
    "D3DTOP_BLENDTEXTUREALPHA",
    "D3DTOP_BLENDFACTORALPHA",
    "D3DTOP_BLENDTEXTUREALPHAPM",
    "D3DTOP_BLENDCURRENTALPHA",
    "D3DTOP_PREMODULATE",
    "D3DTOP_MODULATEALPHA_ADDCOLOR",
    "D3DTOP_MODULATECOLOR_ADDALPHA",
    "D3DTOP_MODULATEINVALPHA_ADDCOLOR",
    "D3DTOP_MODULATEINVCOLOR_ADDALPHA",
    "D3DTOP_BUMPENVMAP",
    "D3DTOP_BUMPENVMAPLUMINANCE",
    "D3DTOP_DOTPRODUCT3",
    "D3DTOP_MULTIPLYADD",
    "D3DTOP_LERP",
    "D3DTOP_FORCE_DWORD",
])

D3DTA = Flags(DWORD, [
    "D3DTA_SELECTMASK",
    "D3DTA_DIFFUSE",
    "D3DTA_CURRENT",
    "D3DTA_TEXTURE",
    "D3DTA_TFACTOR",
    "D3DTA_SPECULAR",
    "D3DTA_TEMP",
    "D3DTA_CONSTANT",
    "D3DTA_COMPLEMENT",
    "D3DTA_ALPHAREPLICATE",
])

D3DTEXTUREFILTERTYPE = Enum("D3DTEXTUREFILTERTYPE", [
    "D3DTEXF_NONE",
    "D3DTEXF_POINT",
    "D3DTEXF_LINEAR",
    "D3DTEXF_ANISOTROPIC",
    "D3DTEXF_PYRAMIDALQUAD",
    "D3DTEXF_GAUSSIANQUAD",
    "D3DTEXF_CONVOLUTIONMONO",
    "D3DTEXF_FORCE_DWORD",
])

D3DPV = Flags(DWORD, [
    "D3DPV_DONOTCOPYDATA",
])

D3DFVF = Flags(DWORD, [
    "D3DFVF_RESERVED0",
    "D3DFVF_POSITION_MASK",
    "D3DFVF_XYZ",
    "D3DFVF_XYZRHW",
    "D3DFVF_XYZB1",
    "D3DFVF_XYZB2",
    "D3DFVF_XYZB3",
    "D3DFVF_XYZB4",
    "D3DFVF_XYZB5",
    "D3DFVF_XYZW",
    "D3DFVF_NORMAL",
    "D3DFVF_PSIZE",
    "D3DFVF_DIFFUSE",
    "D3DFVF_SPECULAR",
    "D3DFVF_TEXCOUNT_MASK",
    "D3DFVF_TEXCOUNT_SHIFT",
    "D3DFVF_TEX0",
    "D3DFVF_TEX1",
    "D3DFVF_TEX2",
    "D3DFVF_TEX3",
    "D3DFVF_TEX4",
    "D3DFVF_TEX5",
    "D3DFVF_TEX6",
    "D3DFVF_TEX7",
    "D3DFVF_TEX8",
    "D3DFVF_LASTBETA_UBYTE4",
    "D3DFVF_LASTBETA_D3DCOLOR",
    "D3DFVF_RESERVED2",
    "D3DFVF_TEXCOORDSIZE3(0)",
    "D3DFVF_TEXCOORDSIZE2(0)",
    "D3DFVF_TEXCOORDSIZE4(0)",
    "D3DFVF_TEXCOORDSIZE1(0)",
    "D3DFVF_TEXCOORDSIZE3(1)",
    "D3DFVF_TEXCOORDSIZE2(1)",
    "D3DFVF_TEXCOORDSIZE4(1)",
    "D3DFVF_TEXCOORDSIZE1(1)",
    "D3DFVF_TEXCOORDSIZE3(2)",
    "D3DFVF_TEXCOORDSIZE2(2)",
    "D3DFVF_TEXCOORDSIZE4(2)",
    "D3DFVF_TEXCOORDSIZE1(2)",
    "D3DFVF_TEXCOORDSIZE3(3)",
    "D3DFVF_TEXCOORDSIZE2(3)",
    "D3DFVF_TEXCOORDSIZE4(3)",
    "D3DFVF_TEXCOORDSIZE1(3)",
])

D3DDECLUSAGE = Enum("D3DDECLUSAGE", [
    "D3DDECLUSAGE_POSITION",
    "D3DDECLUSAGE_BLENDWEIGHT",
    "D3DDECLUSAGE_BLENDINDICES",
    "D3DDECLUSAGE_NORMAL",
    "D3DDECLUSAGE_PSIZE",
    "D3DDECLUSAGE_TEXCOORD",
    "D3DDECLUSAGE_TANGENT",
    "D3DDECLUSAGE_BINORMAL",
    "D3DDECLUSAGE_TESSFACTOR",
    "D3DDECLUSAGE_POSITIONT",
    "D3DDECLUSAGE_COLOR",
    "D3DDECLUSAGE_FOG",
    "D3DDECLUSAGE_DEPTH",
    "D3DDECLUSAGE_SAMPLE",
])

D3DDECLMETHOD = Enum("D3DDECLMETHOD", [
    "D3DDECLMETHOD_DEFAULT",
    "D3DDECLMETHOD_PARTIALU",
    "D3DDECLMETHOD_PARTIALV",
    "D3DDECLMETHOD_CROSSUV",
    "D3DDECLMETHOD_UV",
    "D3DDECLMETHOD_LOOKUP",
    "D3DDECLMETHOD_LOOKUPPRESAMPLED",
])

D3DDECLTYPE = Enum("D3DDECLTYPE", [
    "D3DDECLTYPE_FLOAT1",
    "D3DDECLTYPE_FLOAT2",
    "D3DDECLTYPE_FLOAT3",
    "D3DDECLTYPE_FLOAT4",
    "D3DDECLTYPE_D3DCOLOR",
    "D3DDECLTYPE_UBYTE4",
    "D3DDECLTYPE_SHORT2",
    "D3DDECLTYPE_SHORT4",
    "D3DDECLTYPE_UBYTE4N",
    "D3DDECLTYPE_SHORT2N",
    "D3DDECLTYPE_SHORT4N",
    "D3DDECLTYPE_USHORT2N",
    "D3DDECLTYPE_USHORT4N",
    "D3DDECLTYPE_UDEC3",
    "D3DDECLTYPE_DEC3N",
    "D3DDECLTYPE_FLOAT16_2",
    "D3DDECLTYPE_FLOAT16_4",
    "D3DDECLTYPE_UNUSED",
])

D3DVERTEXELEMENT9 = Struct("D3DVERTEXELEMENT9", [
    (WORD, "Stream"),
    (WORD, "Offset"),
    (BYTE, "Type"),
    (BYTE, "Method"),
    (BYTE, "Usage"),
    (BYTE, "UsageIndex"),
])

D3DSHADER_INSTRUCTION_OPCODE_TYPE = Enum("D3DSHADER_INSTRUCTION_OPCODE_TYPE", [
    "D3DSIO_NOP",
    "D3DSIO_MOV",
    "D3DSIO_ADD",
    "D3DSIO_SUB",
    "D3DSIO_MAD",
    "D3DSIO_MUL",
    "D3DSIO_RCP",
    "D3DSIO_RSQ",
    "D3DSIO_DP3",
    "D3DSIO_DP4",
    "D3DSIO_MIN",
    "D3DSIO_MAX",
    "D3DSIO_SLT",
    "D3DSIO_SGE",
    "D3DSIO_EXP",
    "D3DSIO_LOG",
    "D3DSIO_LIT",
    "D3DSIO_DST",
    "D3DSIO_LRP",
    "D3DSIO_FRC",
    "D3DSIO_M4x4",
    "D3DSIO_M4x3",
    "D3DSIO_M3x4",
    "D3DSIO_M3x3",
    "D3DSIO_M3x2",
    "D3DSIO_CALL",
    "D3DSIO_CALLNZ",
    "D3DSIO_LOOP",
    "D3DSIO_RET",
    "D3DSIO_ENDLOOP",
    "D3DSIO_LABEL",
    "D3DSIO_DCL",
    "D3DSIO_POW",
    "D3DSIO_CRS",
    "D3DSIO_SGN",
    "D3DSIO_ABS",
    "D3DSIO_NRM",
    "D3DSIO_SINCOS",
    "D3DSIO_REP",
    "D3DSIO_ENDREP",
    "D3DSIO_IF",
    "D3DSIO_IFC",
    "D3DSIO_ELSE",
    "D3DSIO_ENDIF",
    "D3DSIO_BREAK",
    "D3DSIO_BREAKC",
    "D3DSIO_MOVA",
    "D3DSIO_DEFB",
    "D3DSIO_DEFI",
    "D3DSIO_TEXCOORD",
    "D3DSIO_TEXKILL",
    "D3DSIO_TEX",
    "D3DSIO_TEXBEM",
    "D3DSIO_TEXBEML",
    "D3DSIO_TEXREG2AR",
    "D3DSIO_TEXREG2GB",
    "D3DSIO_TEXM3x2PAD",
    "D3DSIO_TEXM3x2TEX",
    "D3DSIO_TEXM3x3PAD",
    "D3DSIO_TEXM3x3TEX",
    "D3DSIO_RESERVED0",
    "D3DSIO_TEXM3x3SPEC",
    "D3DSIO_TEXM3x3VSPEC",
    "D3DSIO_EXPP",
    "D3DSIO_LOGP",
    "D3DSIO_CND",
    "D3DSIO_DEF",
    "D3DSIO_TEXREG2RGB",
    "D3DSIO_TEXDP3TEX",
    "D3DSIO_TEXM3x2DEPTH",
    "D3DSIO_TEXDP3",
    "D3DSIO_TEXM3x3",
    "D3DSIO_TEXDEPTH",
    "D3DSIO_CMP",
    "D3DSIO_BEM",
    "D3DSIO_DP2ADD",
    "D3DSIO_DSX",
    "D3DSIO_DSY",
    "D3DSIO_TEXLDD",
    "D3DSIO_SETP",
    "D3DSIO_TEXLDL",
    "D3DSIO_BREAKP",
    "D3DSIO_PHASE",
    "D3DSIO_COMMENT",
    "D3DSIO_END",
    "D3DSIO_FORCE_DWORD",
])

D3DSHADER_COMPARISON = Enum("D3DSHADER_COMPARISON", [
    "D3DSPC_RESERVED0",
    "D3DSPC_GT",
    "D3DSPC_EQ",
    "D3DSPC_GE",
    "D3DSPC_LT",
    "D3DSPC_NE",
    "D3DSPC_LE",
    "D3DSPC_RESERVED1",
])

D3DSAMPLER_TEXTURE_TYPE = Enum("D3DSAMPLER_TEXTURE_TYPE", [
    "D3DSTT_UNKNOWN",
    "D3DSTT_2D",
    "D3DSTT_CUBE",
    "D3DSTT_VOLUME",
    "D3DSTT_FORCE_DWORD",
])

D3DSP = Flags(DWORD, [
    "D3DSP_WRITEMASK_0",
    "D3DSP_WRITEMASK_1",
    "D3DSP_WRITEMASK_2",
    "D3DSP_WRITEMASK_3",
    "D3DSP_WRITEMASK_ALL",
])

D3DSHADER_PARAM_DSTMOD_TYPE = Flags(DWORD, [
    "D3DSPDM_NONE",
    "D3DSPDM_SATURATE",
    "D3DSPDM_PARTIALPRECISION",
    "D3DSPDM_MSAMPCENTROID",
])

D3DSHADER_PARAM_REGISTER_TYPE = Enum("D3DSHADER_PARAM_REGISTER_TYPE", [
    "D3DSPR_TEMP",
    "D3DSPR_INPUT",
    "D3DSPR_CONST",
    "D3DSPR_ADDR|D3DSPR_TEXTURE",
    "D3DSPR_RASTOUT",
    "D3DSPR_ATTROUT",
    "D3DSPR_TEXCRDOUT|D3DSPR_OUTPUT",
    "D3DSPR_CONSTINT",
    "D3DSPR_COLOROUT",
    "D3DSPR_DEPTHOUT",
    "D3DSPR_SAMPLER",
    "D3DSPR_CONST2",
    "D3DSPR_CONST3",
    "D3DSPR_CONST4",
    "D3DSPR_CONSTBOOL",
    "D3DSPR_LOOP",
    "D3DSPR_TEMPFLOAT16",
    "D3DSPR_MISCTYPE",
    "D3DSPR_LABEL",
    "D3DSPR_PREDICATE",
    "D3DSPR_FORCE_DWORD",
])

D3DSHADER_MISCTYPE_OFFSETS = Enum("D3DSHADER_MISCTYPE_OFFSETS", [
    "D3DSMO_POSITION",
    "D3DSMO_FACE",
])

D3DVS_RASTOUT_OFFSETS = Enum("D3DVS_RASTOUT_OFFSETS", [
    "D3DSRO_POSITION",
    "D3DSRO_FOG",
    "D3DSRO_POINT_SIZE",
    "D3DSRO_FORCE_DWORD",
])

D3DVS_ADDRESSMODE_TYPE = Enum("D3DVS_ADDRESSMODE_TYPE", [
    "D3DVS_ADDRMODE_ABSOLUTE",
    "D3DVS_ADDRMODE_RELATIVE",
    "D3DVS_ADDRMODE_FORCE_DWORD",
])

D3DSHADER_ADDRESSMODE_TYPE = Enum("D3DSHADER_ADDRESSMODE_TYPE", [
    "D3DSHADER_ADDRMODE_ABSOLUTE",
    "D3DSHADER_ADDRMODE_RELATIVE",
    "D3DSHADER_ADDRMODE_FORCE_DWORD",
])

D3DVS = Flags(DWORD, [
    "D3DVS_X_X",
    "D3DVS_X_Y",
    "D3DVS_X_Z",
    "D3DVS_X_W",
    "D3DVS_Y_X",
    "D3DVS_Y_Y",
    "D3DVS_Y_Z",
    "D3DVS_Y_W",
    "D3DVS_Z_X",
    "D3DVS_Z_Y",
    "D3DVS_Z_Z",
    "D3DVS_Z_W",
    "D3DVS_W_X",
    "D3DVS_W_Y",
    "D3DVS_W_Z",
    "D3DVS_W_W",
    "D3DVS_NOSWIZZLE",
])

D3DSP = Flags(DWORD, [
    "D3DSP_NOSWIZZLE",
    "D3DSP_REPLICATERED",
    "D3DSP_REPLICATEGREEN",
    "D3DSP_REPLICATEBLUE",
    "D3DSP_REPLICATEALPHA",
])

D3DSHADER_PARAM_SRCMOD_TYPE = Enum("D3DSHADER_PARAM_SRCMOD_TYPE", [
    "D3DSPSM_NONE",
    "D3DSPSM_NEG",
    "D3DSPSM_BIAS",
    "D3DSPSM_BIASNEG",
    "D3DSPSM_SIGN",
    "D3DSPSM_SIGNNEG",
    "D3DSPSM_COMP",
    "D3DSPSM_X2",
    "D3DSPSM_X2NEG",
    "D3DSPSM_DZ",
    "D3DSPSM_DW",
    "D3DSPSM_ABS",
    "D3DSPSM_ABSNEG",
    "D3DSPSM_NOT",
    "D3DSPSM_FORCE_DWORD",
])

D3DBASISTYPE = Enum("D3DBASISTYPE", [
    "D3DBASIS_BEZIER",
    "D3DBASIS_BSPLINE",
    "D3DBASIS_CATMULL_ROM",
    "D3DBASIS_FORCE_DWORD",
])

D3DDEGREETYPE = Enum("D3DDEGREETYPE", [
    "D3DDEGREE_LINEAR",
    "D3DDEGREE_QUADRATIC",
    "D3DDEGREE_CUBIC",
    "D3DDEGREE_QUINTIC",
    "D3DDEGREE_FORCE_DWORD",
])

D3DPATCHEDGESTYLE = Enum("D3DPATCHEDGESTYLE", [
    "D3DPATCHEDGE_DISCRETE",
    "D3DPATCHEDGE_CONTINUOUS",
    "D3DPATCHEDGE_FORCE_DWORD",
])

D3DSTATEBLOCKTYPE = Enum("D3DSTATEBLOCKTYPE", [
    "D3DSBT_ALL",
    "D3DSBT_PIXELSTATE",
    "D3DSBT_VERTEXSTATE",
    "D3DSBT_FORCE_DWORD",
])

D3DVERTEXBLENDFLAGS = Enum("D3DVERTEXBLENDFLAGS", [
    "D3DVBF_DISABLE",
    "D3DVBF_1WEIGHTS",
    "D3DVBF_2WEIGHTS",
    "D3DVBF_3WEIGHTS",
    "D3DVBF_TWEENING",
    "D3DVBF_0WEIGHTS",
    "D3DVBF_FORCE_DWORD",
])

D3DTEXTURETRANSFORMFLAGS = Enum("D3DTEXTURETRANSFORMFLAGS", [
    "D3DTTFF_DISABLE",
    "D3DTTFF_COUNT1",
    "D3DTTFF_COUNT2",
    "D3DTTFF_COUNT3",
    "D3DTTFF_COUNT4",
    "D3DTTFF_PROJECTED",
    "D3DTTFF_FORCE_DWORD",
])

D3DDEVTYPE = Enum("D3DDEVTYPE", [
    "D3DDEVTYPE_HAL",
    "D3DDEVTYPE_REF",
    "D3DDEVTYPE_SW",
    "D3DDEVTYPE_NULLREF",
    "D3DDEVTYPE_FORCE_DWORD",
])

D3DMULTISAMPLE_TYPE = Enum("D3DMULTISAMPLE_TYPE", [
    "D3DMULTISAMPLE_NONE",
    "D3DMULTISAMPLE_NONMASKABLE",
    "D3DMULTISAMPLE_2_SAMPLES",
    "D3DMULTISAMPLE_3_SAMPLES",
    "D3DMULTISAMPLE_4_SAMPLES",
    "D3DMULTISAMPLE_5_SAMPLES",
    "D3DMULTISAMPLE_6_SAMPLES",
    "D3DMULTISAMPLE_7_SAMPLES",
    "D3DMULTISAMPLE_8_SAMPLES",
    "D3DMULTISAMPLE_9_SAMPLES",
    "D3DMULTISAMPLE_10_SAMPLES",
    "D3DMULTISAMPLE_11_SAMPLES",
    "D3DMULTISAMPLE_12_SAMPLES",
    "D3DMULTISAMPLE_13_SAMPLES",
    "D3DMULTISAMPLE_14_SAMPLES",
    "D3DMULTISAMPLE_15_SAMPLES",
    "D3DMULTISAMPLE_16_SAMPLES",
    "D3DMULTISAMPLE_FORCE_DWORD",
])

D3DFORMAT = Enum("D3DFORMAT", [
    "D3DFMT_UNKNOWN",
    "D3DFMT_R8G8B8",
    "D3DFMT_A8R8G8B8",
    "D3DFMT_X8R8G8B8",
    "D3DFMT_R5G6B5",
    "D3DFMT_X1R5G5B5",
    "D3DFMT_A1R5G5B5",
    "D3DFMT_A4R4G4B4",
    "D3DFMT_R3G3B2",
    "D3DFMT_A8",
    "D3DFMT_A8R3G3B2",
    "D3DFMT_X4R4G4B4",
    "D3DFMT_A2B10G10R10",
    "D3DFMT_A8B8G8R8",
    "D3DFMT_X8B8G8R8",
    "D3DFMT_G16R16",
    "D3DFMT_A2R10G10B10",
    "D3DFMT_A16B16G16R16",
    "D3DFMT_A8P8",
    "D3DFMT_P8",
    "D3DFMT_L8",
    "D3DFMT_A8L8",
    "D3DFMT_A4L4",
    "D3DFMT_V8U8",
    "D3DFMT_L6V5U5",
    "D3DFMT_X8L8V8U8",
    "D3DFMT_Q8W8V8U8",
    "D3DFMT_V16U16",
    "D3DFMT_A2W10V10U10",
    "D3DFMT_UYVY",
    "D3DFMT_R8G8_B8G8",
    "D3DFMT_YUY2",
    "D3DFMT_G8R8_G8B8",
    "D3DFMT_DXT1",
    "D3DFMT_DXT2",
    "D3DFMT_DXT3",
    "D3DFMT_DXT4",
    "D3DFMT_DXT5",
    "D3DFMT_D16_LOCKABLE",
    "D3DFMT_D32",
    "D3DFMT_D15S1",
    "D3DFMT_D24S8",
    "D3DFMT_D24X8",
    "D3DFMT_D24X4S4",
    "D3DFMT_D16",
    "D3DFMT_D32F_LOCKABLE",
    "D3DFMT_D24FS8",
    "D3DFMT_D32_LOCKABLE",
    "D3DFMT_S8_LOCKABLE",
    "D3DFMT_L16",
    "D3DFMT_VERTEXDATA",
    "D3DFMT_INDEX16",
    "D3DFMT_INDEX32",
    "D3DFMT_Q16W16V16U16",
    "D3DFMT_MULTI2_ARGB8",
    "D3DFMT_R16F",
    "D3DFMT_G16R16F",
    "D3DFMT_A16B16G16R16F",
    "D3DFMT_R32F",
    "D3DFMT_G32R32F",
    "D3DFMT_A32B32G32R32F",
    "D3DFMT_CxV8U8",
    "D3DFMT_A1",
    "D3DFMT_BINARYBUFFER",
    "D3DFMT_FORCE_DWORD",
])

D3DDISPLAYMODE = Struct("D3DDISPLAYMODE", [
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "RefreshRate"),
    (D3DFORMAT, "Format"),
])

D3DDEVICE_CREATION_PARAMETERS = Struct("D3DDEVICE_CREATION_PARAMETERS", [
    (UINT, "AdapterOrdinal"),
    (D3DDEVTYPE, "DeviceType"),
    (HWND, "hFocusWindow"),
    (DWORD, "BehaviorFlags"),
])

D3DSWAPEFFECT = Enum("D3DSWAPEFFECT", [
    "D3DSWAPEFFECT_DISCARD",
    "D3DSWAPEFFECT_FLIP",
    "D3DSWAPEFFECT_COPY",
    "D3DSWAPEFFECT_FORCE_DWORD",
])

D3DPOOL = Enum("D3DPOOL", [
    "D3DPOOL_DEFAULT",
    "D3DPOOL_MANAGED",
    "D3DPOOL_SYSTEMMEM",
    "D3DPOOL_SCRATCH",
    "D3DPOOL_FORCE_DWORD",
])

D3DPRESENT = Flags(DWORD, [
    "D3DPRESENT_RATE_DEFAULT",
])

D3DPRESENT_PARAMETERS = Struct("D3DPRESENT_PARAMETERS", [
    (UINT, "BackBufferWidth"),
    (UINT, "BackBufferHeight"),
    (D3DFORMAT, "BackBufferFormat"),
    (UINT, "BackBufferCount"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (DWORD, "MultiSampleQuality"),
    (D3DSWAPEFFECT, "SwapEffect"),
    (HWND, "hDeviceWindow"),
    (BOOL, "Windowed"),
    (BOOL, "EnableAutoDepthStencil"),
    (D3DFORMAT, "AutoDepthStencilFormat"),
    (DWORD, "Flags"),
    (UINT, "FullScreen_RefreshRateInHz"),
    (UINT, "PresentationInterval"),
])

D3DPRESENTFLAG = Flags(DWORD, [
    "D3DPRESENTFLAG_LOCKABLE_BACKBUFFER",
    "D3DPRESENTFLAG_DISCARD_DEPTHSTENCIL",
    "D3DPRESENTFLAG_DEVICECLIP",
    "D3DPRESENTFLAG_VIDEO",
    "D3DPRESENTFLAG_NOAUTOROTATE",
    "D3DPRESENTFLAG_UNPRUNEDMODE",
])

D3DGAMMARAMP = Struct("D3DGAMMARAMP", [
    (WORD, "red[256]"),
    (WORD, "green[256]"),
    (WORD, "blue[256]"),
])

D3DBACKBUFFER_TYPE = Enum("D3DBACKBUFFER_TYPE", [
    "D3DBACKBUFFER_TYPE_MONO",
    "D3DBACKBUFFER_TYPE_LEFT",
    "D3DBACKBUFFER_TYPE_RIGHT",
    "D3DBACKBUFFER_TYPE_FORCE_DWORD",
])

D3DRESOURCETYPE = Enum("D3DRESOURCETYPE", [
    "D3DRTYPE_SURFACE",
    "D3DRTYPE_VOLUME",
    "D3DRTYPE_TEXTURE",
    "D3DRTYPE_VOLUMETEXTURE",
    "D3DRTYPE_CUBETEXTURE",
    "D3DRTYPE_VERTEXBUFFER",
    "D3DRTYPE_INDEXBUFFER",
    "D3DRTYPE_FORCE_DWORD",
])

D3DUSAGE = Flags(DWORD, [
    "D3DUSAGE_RENDERTARGET",
    "D3DUSAGE_DEPTHSTENCIL",
    "D3DUSAGE_DYNAMIC",
    "D3DUSAGE_NONSECURE",
    "D3DUSAGE_AUTOGENMIPMAP",
    "D3DUSAGE_DMAP",
    "D3DUSAGE_QUERY_LEGACYBUMPMAP",
    "D3DUSAGE_QUERY_SRGBREAD",
    "D3DUSAGE_QUERY_FILTER",
    "D3DUSAGE_QUERY_SRGBWRITE",
    "D3DUSAGE_QUERY_POSTPIXELSHADER_BLENDING",
    "D3DUSAGE_QUERY_VERTEXTEXTURE",
    "D3DUSAGE_QUERY_WRAPANDMIP",
    "D3DUSAGE_WRITEONLY",
    "D3DUSAGE_SOFTWAREPROCESSING",
    "D3DUSAGE_DONOTCLIP",
    "D3DUSAGE_POINTS",
    "D3DUSAGE_RTPATCHES",
    "D3DUSAGE_NPATCHES",
    "D3DUSAGE_TEXTAPI",
])

D3DCUBEMAP_FACES = Enum("D3DCUBEMAP_FACES", [
    "D3DCUBEMAP_FACE_POSITIVE_X",
    "D3DCUBEMAP_FACE_NEGATIVE_X",
    "D3DCUBEMAP_FACE_POSITIVE_Y",
    "D3DCUBEMAP_FACE_NEGATIVE_Y",
    "D3DCUBEMAP_FACE_POSITIVE_Z",
    "D3DCUBEMAP_FACE_NEGATIVE_Z",
    "D3DCUBEMAP_FACE_FORCE_DWORD",
])

D3DLOCK = Flags(DWORD, [
    "D3DLOCK_READONLY",
    "D3DLOCK_DISCARD",
    "D3DLOCK_NOOVERWRITE",
    "D3DLOCK_NOSYSLOCK",
    "D3DLOCK_DONOTWAIT",
    "D3DLOCK_NO_DIRTY_UPDATE",
])

D3DVERTEXBUFFER_DESC = Struct("D3DVERTEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
    (DWORD, "FVF"),
])

D3DINDEXBUFFER_DESC = Struct("D3DINDEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
])

D3DSURFACE_DESC = Struct("D3DSURFACE_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (DWORD, "MultiSampleQuality"),
    (UINT, "Width"),
    (UINT, "Height"),
])

D3DVOLUME_DESC = Struct("D3DVOLUME_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Depth"),
])

D3DLOCKED_RECT = Struct("D3DLOCKED_RECT", [
    (INT, "Pitch"),
    (OpaquePointer(Void), "pBits"),
])

D3DBOX = Struct("D3DBOX", [
    (UINT, "Left"),
    (UINT, "Top"),
    (UINT, "Right"),
    (UINT, "Bottom"),
    (UINT, "Front"),
    (UINT, "Back"),
])

D3DLOCKED_BOX = Struct("D3DLOCKED_BOX", [
    (INT, "RowPitch"),
    (INT, "SlicePitch"),
    (OpaquePointer(Void), "pBits"),
])

D3DRANGE = Struct("D3DRANGE", [
    (UINT, "Offset"),
    (UINT, "Size"),
])

D3DRECTPATCH_INFO = Struct("D3DRECTPATCH_INFO", [
    (UINT, "StartVertexOffsetWidth"),
    (UINT, "StartVertexOffsetHeight"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Stride"),
    (D3DBASISTYPE, "Basis"),
    (D3DDEGREETYPE, "Degree"),
])

D3DTRIPATCH_INFO = Struct("D3DTRIPATCH_INFO", [
    (UINT, "StartVertexOffset"),
    (UINT, "NumVertices"),
    (D3DBASISTYPE, "Basis"),
    (D3DDEGREETYPE, "Degree"),
])

D3DADAPTER_IDENTIFIER9 = Struct("D3DADAPTER_IDENTIFIER9", [
    (CString, "Driver"),
    (CString, "Description"),
    (CString, "DeviceName"),
    (LARGE_INTEGER, "DriverVersion"),
    (DWORD, "VendorId"),
    (DWORD, "DeviceId"),
    (DWORD, "SubSysId"),
    (DWORD, "Revision"),
    (GUID, "DeviceIdentifier"),
    (DWORD, "WHQLLevel"),
])

D3DRASTER_STATUS = Struct("D3DRASTER_STATUS", [
    (BOOL, "InVBlank"),
    (UINT, "ScanLine"),
])

D3DDEBUGMONITORTOKENS = Enum("D3DDEBUGMONITORTOKENS", [
    "D3DDMT_ENABLE",
    "D3DDMT_DISABLE",
    "D3DDMT_FORCE_DWORD",
])

D3DQUERYTYPE = Enum("D3DQUERYTYPE", [
    "D3DQUERYTYPE_VCACHE",
    "D3DQUERYTYPE_RESOURCEMANAGER",
    "D3DQUERYTYPE_VERTEXSTATS",
    "D3DQUERYTYPE_EVENT",
    "D3DQUERYTYPE_OCCLUSION",
    "D3DQUERYTYPE_TIMESTAMP",
    "D3DQUERYTYPE_TIMESTAMPDISJOINT",
    "D3DQUERYTYPE_TIMESTAMPFREQ",
    "D3DQUERYTYPE_PIPELINETIMINGS",
    "D3DQUERYTYPE_INTERFACETIMINGS",
    "D3DQUERYTYPE_VERTEXTIMINGS",
    "D3DQUERYTYPE_PIXELTIMINGS",
    "D3DQUERYTYPE_BANDWIDTHTIMINGS",
    "D3DQUERYTYPE_CACHEUTILIZATION",
])

D3DISSUE = Flags(DWORD, [
    "D3DISSUE_END",
    "D3DISSUE_BEGIN",
])

D3DGETDATA = Flags(DWORD, [
    "D3DGETDATA_FLUSH",
])

D3DRESOURCESTATS = Struct("D3DRESOURCESTATS", [
    (BOOL, "bThrashing"),
    (DWORD, "ApproxBytesDownloaded"),
    (DWORD, "NumEvicts"),
    (DWORD, "NumVidCreates"),
    (DWORD, "LastPri"),
    (DWORD, "NumUsed"),
    (DWORD, "NumUsedInVidMem"),
    (DWORD, "WorkingSet"),
    (DWORD, "WorkingSetBytes"),
    (DWORD, "TotalManaged"),
    (DWORD, "TotalBytes"),
])

D3DDEVINFO_RESOURCEMANAGER = Struct("D3DDEVINFO_RESOURCEMANAGER", [
    (D3DRESOURCESTATS, "stats[D3DRTYPECOUNT]"),
    (D3DRESOURCESTATS, "stats[8]"),
])

D3DDEVINFO_D3DVERTEXSTATS = Struct("D3DDEVINFO_D3DVERTEXSTATS", [
    (DWORD, "NumRenderedTriangles"),
    (DWORD, "NumExtraClippingTriangles"),
])

D3DDEVINFO_VCACHE = Struct("D3DDEVINFO_VCACHE", [
    (DWORD, "Pattern"),
    (DWORD, "OptMethod"),
    (DWORD, "CacheSize"),
    (DWORD, "MagicNumber"),
])

D3DDEVINFO_D3D9PIPELINETIMINGS = Struct("D3DDEVINFO_D3D9PIPELINETIMINGS", [
    (FLOAT, "VertexProcessingTimePercent"),
    (FLOAT, "PixelProcessingTimePercent"),
    (FLOAT, "OtherGPUProcessingTimePercent"),
    (FLOAT, "GPUIdleTimePercent"),
])

D3DDEVINFO_D3D9INTERFACETIMINGS = Struct("D3DDEVINFO_D3D9INTERFACETIMINGS", [
    (FLOAT, "WaitingForGPUToUseApplicationResourceTimePercent"),
    (FLOAT, "WaitingForGPUToAcceptMoreCommandsTimePercent"),
    (FLOAT, "WaitingForGPUToStayWithinLatencyTimePercent"),
    (FLOAT, "WaitingForGPUExclusiveResourceTimePercent"),
    (FLOAT, "WaitingForGPUOtherTimePercent"),
])

D3DDEVINFO_D3D9STAGETIMINGS = Struct("D3DDEVINFO_D3D9STAGETIMINGS", [
    (FLOAT, "MemoryProcessingPercent"),
    (FLOAT, "ComputationProcessingPercent"),
])

D3DDEVINFO_D3D9BANDWIDTHTIMINGS = Struct("D3DDEVINFO_D3D9BANDWIDTHTIMINGS", [
    (FLOAT, "MaxBandwidthUtilized"),
    (FLOAT, "FrontEndUploadMemoryUtilizedPercent"),
    (FLOAT, "VertexRateUtilizedPercent"),
    (FLOAT, "TriangleSetupRateUtilizedPercent"),
    (FLOAT, "FillRateUtilizedPercent"),
])

D3DDEVINFO_D3D9CACHEUTILIZATION = Struct("D3DDEVINFO_D3D9CACHEUTILIZATION", [
    (FLOAT, "TextureCacheHitRate"),
    (FLOAT, "PostTransformVertexCacheHitRate"),
])

D3DCOMPOSERECTSOP = Enum("D3DCOMPOSERECTSOP", [
    "D3DCOMPOSERECTS_COPY",
    "D3DCOMPOSERECTS_OR",
    "D3DCOMPOSERECTS_AND",
    "D3DCOMPOSERECTS_NEG",
    "D3DCOMPOSERECTS_FORCE_DWORD",
])

D3DCOMPOSERECTDESC = Struct("D3DCOMPOSERECTDESC", [
    (USHORT, "X"),
    (USHORT, "Y"),
    (USHORT, "Width"),
    (USHORT, "Height"),
])

D3DCOMPOSERECTDESTINATION = Struct("D3DCOMPOSERECTDESTINATION", [
    (USHORT, "SrcRectIndex"),
    (USHORT, "Reserved"),
    (Short, "X"),
    (Short, "Y"),
])

D3DPRESENTSTATS = Struct("D3DPRESENTSTATS", [
    (UINT, "PresentCount"),
    (UINT, "PresentRefreshCount"),
    (UINT, "SyncRefreshCount"),
    (LARGE_INTEGER, "SyncQPCTime"),
    (LARGE_INTEGER, "SyncGPUTime"),
])

D3DSCANLINEORDERING = Enum("D3DSCANLINEORDERING", [
    "D3DSCANLINEORDERING_UNKNOWN",
    "D3DSCANLINEORDERING_PROGRESSIVE",
    "D3DSCANLINEORDERING_INTERLACED",
])

D3DDISPLAYMODEEX = Struct("D3DDISPLAYMODEEX", [
    (UINT, "Size"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "RefreshRate"),
    (D3DFORMAT, "Format"),
    (D3DSCANLINEORDERING, "ScanLineOrdering"),
])

D3DDISPLAYMODEFILTER = Struct("D3DDISPLAYMODEFILTER", [
    (UINT, "Size"),
    (D3DFORMAT, "Format"),
    (D3DSCANLINEORDERING, "ScanLineOrdering"),
])

D3DDISPLAYROTATION = Enum("D3DDISPLAYROTATION", [
    "D3DDISPLAYROTATION_IDENTITY",
    "D3DDISPLAYROTATION_90",
    "D3DDISPLAYROTATION_180",
    "D3DDISPLAYROTATION_270",
])

D3D9_RESOURCE_PRIORITY = Flags(DWORD, [
    "D3D9_RESOURCE_PRIORITY_MINIMUM",
    "D3D9_RESOURCE_PRIORITY_LOW",
    "D3D9_RESOURCE_PRIORITY_NORMAL",
    "D3D9_RESOURCE_PRIORITY_HIGH",
    "D3D9_RESOURCE_PRIORITY_MAXIMUM",
])

