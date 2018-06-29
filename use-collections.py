#/usr/bin/env python3
# coding: utf-8

import collections


Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p, p.x, p.y)

dq = collections.deque(['a'])
dq.append('b')
print(dq)

dd = collections.defaultdict(lambda: None)
print(dd, type(dd), dd['a'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
d2 = {
    'a': 1,
    'b': 2,
    'c': 3,
}
print(d, d2)


od = collections.OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od, od.keys())


c = collections.Counter(a=1, b=2)
print(c)
