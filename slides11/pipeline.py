#!/usr/bin/env python3

import os

os.system('ps aux | wc -l')

import subprocess

ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
wc = subprocess.run(['wc', '-l'], stdin=ps.stdout, stdout=subprocess.PIPE)

print(wc.stdout.decode(), end='')
