#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for arg in sys.argv[:0:-1]:
        print(arg)