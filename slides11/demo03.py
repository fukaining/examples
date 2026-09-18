#!/usr/bin/env python3

import os

'''
Pipelines: Demonstration (3)

Who has the most processes on student10.cse.nd.edu?
'''

# Python Solution

counts = {}
for line in os.popen('ps aux'):
    user = line.split()[0]
    counts[user] = counts.get(user, 0) + 1

max_user = list(counts.keys())[0]
for user, count in counts.items():
    if count > counts[max_user]:
        max_user = user

print(max_user)

# Pipeline Solution
os.system("ps aux | awk '{print $1}' | sort | uniq -c | sort -rn | head -n 1 | awk '{print $2}'")
