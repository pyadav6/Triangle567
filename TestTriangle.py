# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from brand import my_brand
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
my_brand_here = False
my_brand("HW 02a - Testing a legacy program and reporting on testing results")
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(6,7,5),'Scalene','4,4,5 is a Scalene triangle')

    def testSideUpperLimitTriangleA(self): 
        self.assertEqual(classifyTriangle(201,4,5),'InvalidInputOne','201,4,5 is a InvalidInput')

    def testSideLowerLimitTriangleA(self): 
        self.assertEqual(classifyTriangle(4,0,-5),'InvalidInputTwo','4,0,5 is a InvalidInput')

    def testInputDatatypeTriangleA(self): 
        self.assertEqual(classifyTriangle(4,1.5,5),'InvalidInputThree','4,0,5 is a InvalidInput')

    def testFormationTriangleA(self): 
        self.assertEqual(classifyTriangle(2,3,6),'NotATriangle','2,3,6 is a NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)

if not my_brand_here:
    my_brand("HW 02a - Testing a legacy program and reporting on testing results")

