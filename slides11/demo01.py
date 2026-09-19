#!/usr/bin/env python3

import os
import subprocess

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

subprocess.run('ps aux | grep -v grep | grep bash | wc -l', shell=True)
