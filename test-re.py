#/usr/bin/env python3
# coding: utf-8

import re


s = '1234abc'
pattern = r'(\d+)(\w+)'
m = re.match(pattern, s)
print('matched=>', m, m.groups())

#compile
re_compile = re.compile(pattern)
m = re_compile.match(s)
print('use compile m=>', m, m.groups())
