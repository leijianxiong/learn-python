#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Test(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value



t = Test()
t.score = 12
print('t.score =', t.score)