#!/usr/bin/env python3

import os
import re

path = '/usr/share/dict/words'

os.system(f"cat {path} | grep -E '^([ao]).{{3}}\\1$'")

with open(path) as stream:
    for line in stream:
        if m := re.search(r'^([ao]).{3}\1$', line):
            print(m[0])
