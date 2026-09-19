#!/usr/bin/env python3

import os

text = 'burn this city'

os.system(f'echo {text} | tr abc xyz')
print(text.translate(str.maketrans('abc', 'xyz')))

os.system(f'echo {text} | tr a-z A-Z')
print(text.upper())

os.system(f'echo {text} | tr -d " "')
print(text.replace(' ', ''))
