#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sunyongzhen

class Mammal(object):
    extremities = 4
    def feeds(self):
        print("milk")
    def proliferate(self):
        pass

class Marsupial(Mammal):
    """ this a class """

    def __init__(self):
        """ Constructor for class Marsupial """
        pass

    def proliferate(self):
        print("poach")

class Eutherian(Mammal):
    """ this a class """

    def __init__(self):
        """ Constructor for class Marsupial """
        pass

    def proliferate(self):
        print("placenta")