#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试类属性++"""


class Student(object):
    count = 0

    '''
    this is comment
    '''
    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败! 1')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败! 2')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败! 3')
        else:
            print('Students:', Student.count)
            print('测试通过! 4')