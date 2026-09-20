#!/usr/bin/env python3

import os

os.system('ps aux | grep pbui | wc -l')

from subprocess import Popen, PIPE, DEVNULL, run

ps   = Popen(['ps', 'aux'], stdout=PIPE, stderr=DEVNULL)
grep = Popen(['grep', 'pbui'], stdin=ps.stdout, stdout=PIPE)
wc   = run(['wc', '-l'], stdin=grep.stdout, stdout=PIPE)

print(wc.stdout.decode(), end='')
