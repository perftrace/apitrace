#!/usr/bin/env python
##########################################################################
#
# Copyright 2011 Jose Fonseca
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/


import difflib
import optparse
import os.path
import re
import subprocess
import sys


call_re = re.compile('^([0-9]+) (\w+)\(')

ansi_re = re.compile('\x1b\[[0-9]{1,2}(;[0-9]{1,2}){0,2}m')


def ansi_strip(s):
    # http://www.theeggeadventure.com/wikimedia/index.php/Linux_Tips#Use_sed_to_remove_ANSI_colors
    return ansi_re.sub('', s)


ignored_function_names = set([
    'glGetString',
    'glXGetClientString',
    'glXGetCurrentDisplay',
    'glXGetProcAddress',
    'glXGetProcAddressARB',
    'wglGetProcAddress',
])


def readtrace(trace):
    p = subprocess.Popen([options.tracedump, trace], stdout=subprocess.PIPE)
    lines = []
    for line in p.stdout.readlines():
        line = ansi_strip(line)
        mo = call_re.match(line)
        if mo:
            function_name = mo.group(2)
            if function_name in ignored_function_names:
                continue
            lines.append(line[mo.start(2):])
        else:
            lines[-1] += line
    p.wait()
    return lines


def main():
    global options

    optparser = optparse.OptionParser(
        usage='\n\t%prog <trace> <trace>',
        version='%%prog')
    optparser.add_option(
        '-d', '--tracedump', metavar='PROGRAM',
        type='string', dest='tracedump', default='tracedump',
        help='tracedump command [default: %default]')

    (options, args) = optparser.parse_args(sys.argv[1:])
    if len(args) != 2:
        optparser.error("incorrect number of arguments")

    ref_lines = readtrace(args[0])
    src_lines = readtrace(args[1])

    diff = difflib.unified_diff(ref_lines, src_lines, n=3)
    sys.stdout.writelines(diff)


if __name__ == '__main__':
    main()
