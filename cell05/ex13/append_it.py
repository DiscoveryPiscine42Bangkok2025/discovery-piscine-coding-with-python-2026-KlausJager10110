#!/usr/bin/env python

import sys
import re

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        if re.search(r'ism$', arg):
            continue
        print(f"{arg}ism")

