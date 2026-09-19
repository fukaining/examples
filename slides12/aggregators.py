#!/usr/bin/env python3

import os

path = '/etc/hosts'

with open(path) as stream:
    lines = stream.readlines()

os.system(f'cat {path} | head -n 3')
print(''.join(lines[:3]), end='')

os.system(f'cat {path} | tail -n 3')
print(''.join(lines[-3:]), end='')

os.system(f'cat {path} | wc -l')
print(len(lines))

os.system(f'cat {path} | sort | uniq | wc -l')
print(len(set(lines)))
