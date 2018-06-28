#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""__slots__只在当前类生效, 子类支持范围为子类+父类__slots__"""

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    __slots__ = ('height')
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.name = 99
print('g.name =', g.name)
