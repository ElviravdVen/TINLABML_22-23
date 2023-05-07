#!/usr/bin/env python

from tensors import Vector
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class TestVector(unittest.TestCase):
    vectorA = Vector( [1, 1] )
    vectorB = Vector( [-1, -1] )
    vectorC = Vector( [1, -1] )

    def getDimensions(self):
        self.assertEqual(self.vectorB.getDimensions(), (2, 1))

    # Test Addition of Vectors
    def testAdd(self):
        self.assertEqual(self.vectorA + self.vectorB, (0.0, 0.0))

    # Test Multiplication of Vectors
    def testMult(self):
        self.assertEqual(self.vectorA * self.vectorC, 0.0)    

    # Test String representation of Vector
    def testStr(self):
        self.assertEqual(str(self.vectorC), "[1.0, -1.0]")

if __name__ == '__main__':
    unittest.main()