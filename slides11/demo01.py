#!/usr/bin/env python3

import os

'''
Pipelines: Demonstration (1)

How many bash processes are there on student10.cse.nd.edu?
'''

# Python Solution

count = 0
for line in os.popen('ps aux'):
    if 'bash' in line:
        count += 1

print(count)

# Pipeline Solution
os.system('ps aux | grep -v grep | grep bash | wc -l')
