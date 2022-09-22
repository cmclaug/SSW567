# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Caitlin McLaughlin
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')   

    def testNotATriangles(self): 
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 should be NotATriangle')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(1,3,4),'Scalene','1,3,4 should be scalene')   

    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isosceles','1,2,2 should be Isosceles')

    def testInvalidTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,3),'Invalid','1,1,3 should be Invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

