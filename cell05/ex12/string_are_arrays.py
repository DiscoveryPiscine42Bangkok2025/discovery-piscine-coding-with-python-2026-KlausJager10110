#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    found = False
    
    for c in s:
        if c == 'z':
            print('z', end='')
            found = True

    if not found:
        print("none")
    else:
        pass