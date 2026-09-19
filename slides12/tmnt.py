#!/usr/bin/env python3

import os
import re

path = 'tmnt.txt'

# 1. List only the **colors** of the turtles.

os.system(f"cat {path} | awk '{{print $2}}'")

with open(path) as stream:
    for line in stream:
        print(line.split()[1])

# 2. List only the **turtles** whose names end in lo.

os.system(f"cat {path} | awk '{{print $1}}' | grep -E 'lo$'")

with open(path) as stream:
    for line in stream:
        turtle = line.split()[0]
        if turtle.endswith('lo'):
            print(turtle)

# 3. List the **colors** that don't end with a vowel.

os.system(f"cat {path} | awk '{{print $3}}' | grep -E '[^aeiou]$'")

with open(path) as stream:
    for line in stream:
        weapon = line.split()[2]
        if m := re.search(r'[^aeiou]$', weapon):
            print(weapon)
