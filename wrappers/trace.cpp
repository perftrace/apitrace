/**************************************************************************
 *
 * Copyright 2010-2011 VMware, Inc.
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


#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef ANDROID
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/system_properties.h>
#endif

#include "os.hpp"
#include "os_string.hpp"
#include "os_process.hpp"
#include "trace.hpp"


namespace trace {

static bool s_checkedEnv = false;
static bool s_singleFrameTraceEnabled = false;
static unsigned long s_frameNumToTrace = 0;
static unsigned long s_currentFrameNum = 0;

void incrementFrameNumber(void) {
    ++s_currentFrameNum;
    if (isFrameToTrace() && s_singleFrameTraceEnabled)
    {
        snapshotState();
    }
}

bool isTracingStateSetupFunctions(void)
{
    return s_singleFrameTraceEnabled && (s_currentFrameNum <= s_frameNumToTrace);
}

bool isFrameToTrace(void) {
    if ( !s_checkedEnv ) {
        s_checkedEnv = true;
        const char* strFrame = getenv( "TRACE_FRAME" );
        os::unsetEnvironment("TRACE_FRAME");
        s_singleFrameTraceEnabled = ( strFrame != NULL );
        if ( s_singleFrameTraceEnabled ) {
            s_frameNumToTrace = strtoul( strFrame, NULL, 10 );
        }
    }

    if ( !s_singleFrameTraceEnabled )
    {
        return true;
    } else {
        return s_currentFrameNum == s_frameNumToTrace;
    }
}

#ifdef ANDROID

static bool
isZygoteProcess(void)
{
    os::String proc_name;

    proc_name = os::getProcessName();
    proc_name.trimDirectory();

    return strcmp(proc_name, "app_process") == 0;
}

static os::String
getZygoteProcessName(void)
{
    os::String path;
    size_t size = PATH_MAX;
    char *buf = path.buf(size);
    ssize_t len;

    int fd = open("/proc/self/cmdline", O_RDONLY);

    assert(fd >= 0);
    len = read(fd, buf, size - 1);
    close(fd);
    path.truncate(len);

    return path;
}

bool
isTracingEnabled(void)
{
    if (!isFrameToTrace()) {
        return false;
    }

    static pid_t cached_pid;
    static bool enabled;
    pid_t pid;

    pid = getpid();
    if (cached_pid == pid)
        return enabled;
    cached_pid = pid;

    if (!isZygoteProcess()) {
        os::log("apitrace[%d]: enabled for standalone %s",
                pid, (const char *)os::getProcessName());
        enabled = true;
        return true;
    }

    char target_proc_name[PROP_VALUE_MAX] = "";
    os::String proc_name;

    proc_name = getZygoteProcessName();
    proc_name.trimDirectory();

    __system_property_get("debug.apitrace.procname", target_proc_name);
    enabled = !strcmp(target_proc_name, proc_name);
    os::log("apitrace[%d]: %s for %s",
            pid, enabled ? "enabled" : "disabled", (const char *)proc_name);

    return enabled;
}

#endif /* ANDROID */


} /* namespace trace */
