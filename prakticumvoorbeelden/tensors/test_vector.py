#!/usr/bin/env python

from tensors import Vector
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class TestVector(unittest.TestCase):
    vectorA = Vector( [1, 1] )
    vectorB = Vector( [-1, -1] )
    vectorC = Vector( [0, 1, 2, 3, 4] )

    # Test length of Vector
    def testLen(self):
        self.assertEqual(len(self.vectorA), 2)

    # Test Addition of Vectors
    def testAdd(self):
        self.assertEqual(self.vectorA + self.vectorB, (0.0, 0.0))

    # # Test Multiplication of Vectors
    # def testMult(self):
    #     self.assertEqual(self.vectorA * self.vectorB, (0.0, 0.0))    

    # def testStr(self):
    #     self.assertEqual(str(self.VectorB), "-1.0")

    def getDimensions(self):
        self.assertEqual(self.vectorB.getDimensions(), 5)

if __name__ == '__main__':
    unittest.main()