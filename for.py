#!/usr/bin/env python3
# coding: utf-8

for row in range(1, 10):
    for column in range(1, row+1):
        print('%s x %s = %s ' % (column, row, row * column), end='')
    print("\r")
