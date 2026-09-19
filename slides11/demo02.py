#!/usr/bin/env python3

import os
import subprocess

'''
Pipelines: Demonstration (2)

How many different users processes are on there on student10.cse.nd.edu?
'''

# Python Solution

users = set()
for line in os.popen('ps aux'):
    user = line.split()[0]
    users.add(user)

print(len(users))

# Pipeline Solution

subprocess.run("ps aux | awk '{print $1}' | sort | uniq | wc -l", shell=True)
