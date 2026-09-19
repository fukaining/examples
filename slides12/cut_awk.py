#!/usr/bin/env python3

import os

text = 'burn this city'

os.system(f'echo {text} | cut -d " " -f 1')
os.system(f"echo {text} | awk '{{print $1}}'")
print(text.split()[0])

os.system(f'echo {text} | cut -d " " -f 1,3')
os.system(f"echo {text} | awk '{{print $1, $3}}'")
print(text.split()[0], text.split()[2])

os.system(f'echo {text} | cut -c 2-4')
print(text[1:4])
