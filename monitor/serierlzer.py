#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sunyzh
import math

class Solver():
    """ this a class """

    def __init__(self, name, age):
        """ Constructor for class Solver """
        self.name = name
        self.age = age

    def print_string(self):
        print "hello %s, and your age is %s" % (self.name, self.age)

class Solver2():
    """  """

    def __init__(self, ):
        """ Constructor for class Solver2 """

        


if __name__ == '__main__':
    solver = Solver("sunyzh",30)
    solver.print_string()