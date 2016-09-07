#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sunyzh
import math


class Solver(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_string(self):
        for i in range(1,5):

            try:
                math.acos(30)
                num = i
            except:
                pass



            print "hello solver..%s,%d" % (self.name, self.age)


if __name__ == '__main__':
    solver = Solver("sunyzh",30)
    solver.print_string()