#!/usr/bin/env python3

import os
import re

path = '/etc/hosts'

os.system(f"cat {path} | sed -E 's/[0-9]{{1,3}}/x/g'")

with open(path) as stream:
    for line in stream:
        print(re.sub(r'[0-9]{1,3}', 'x', line), end='')
