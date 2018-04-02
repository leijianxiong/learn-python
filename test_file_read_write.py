#!/usr/bin/env python3
# coding: utf-8

"""
"""

import os
import pickle
import json

path = 'message.txt'
# with open(path, 'r') as f:
#     lines = f.readlines()
# print(lines)
# print("test", lines[0][:-2].strip() == '', "test")
# lines = list(filter(lambda x: x[:-2].strip() != '', lines))
# print(lines)

# with open(path, 'r') as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         line = line[:-2]
#         if (line.strip() == ''):
#             continue
#         if line.split(',')[0] == 1:
#             continue
#         print(i, line, line.split(',')[0] == str(1))

# l = ['a', 'b', 'c']
# print(l[-1])

#
s = '2,bb,jianxiong'
print(s.split(',')[0])


def mk_int(s):
    s = s.strip()
    return int(s) if s else 0


print(mk_int(' '), len([]), int('' or 0))

serialized_str = pickle.dumps("multi\nline")
print(serialized_str, pickle.loads(serialized_str))

print(json.loads(json.dumps("multi\nline")))
print(json.loads('"a"'))
