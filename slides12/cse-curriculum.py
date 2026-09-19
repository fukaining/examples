#!/usr/bin/env python3

import os
import re
import requests

URL = 'https://yld.me/mbfL'

# 1. How many MATH vs PHYS vs CSE courses?

os.system(f"""
curl -sL {URL} \
        | grep -Eo '(MATH|PHYS|CSE) [0-9]{{5}}' \
        | awk '{{print $1}}' \
        | sort | uniq -c
""")

response = requests.get(URL)
counts   = {}

for line in response.text.splitlines():
    for department in re.findall(r'(MATH|PHYS|CSE) [0-9]{5}', line):
        counts[department] = counts.get(department, 0) + 1

for department, count in sorted(counts.items()):
    print(f'{count:>7} {department}')

# 2. How many sophomore CSE courses?

os.system(f"""
curl -sL {URL} \
        | grep -Eo 'CSE 2[0-9]{{4}}' \
        | awk '{{print $1}}' \
        | wc -l
""")

response = requests.get(URL)
courses  = re.findall(r'CSE 2[0-9]{4}', response.text, flags=re.MULTILINE)
print(len(courses))
