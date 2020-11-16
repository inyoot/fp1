# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:03:41 2020

@author: isandjaja
"""
from math import sqrt
class Point2D():
    """ Point in two dimension
    You can create with two argument x and y
    distance() will calculate the distance from the origin
    """
    def __init__(self, x=0 ,y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "{}, {}".format(self.x, self.y)
    
    def distance(self):
        return sqrt(self.x**2 + self.y**2)
    
