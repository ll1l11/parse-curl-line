# -*- coding: utf-8 -*-
import re
import os.path

PATTERN = re.compile('(?:^(-[\w:#]+), )?(--[\w\-\.:]+)(?:$|\s+.*$$)')

path = os.path.join(os.path.dirname(__file__), 'curl-options.txt')
print('*' * 20, path)


options = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        m = PATTERN.match(line)
        if m:
            options.append(m.groups())
print('#', len(options))
print(options)

for option in options:
    args = ', '.join(["'{0}'".format(x) for x in option if x])
    print("parser.add_argument({0})".format(args))
