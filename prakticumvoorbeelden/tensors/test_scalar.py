#!/usr/bin/env python

from tensors import Scalar
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class TestScalar(unittest.TestCase):
    scalarA = Scalar(1)
    scalarB = Scalar(-1)
    scalarC = Scalar(0)

    # Test Addition of Scalars
    def testAdd(self):
        self.assertEqual(self.scalarA + self.scalarB, 0)

    def testMult(self):
        self.assertEqual(self.scalarA * self.scalarC, 0)    

    def testStr(self):
        self.assertEqual(str(self.scalarB), "-1.0")

    def testGetDimensions(self):
        self.assertEqual(self.scalarC.getDimensions(), (1, 1))

if __name__ == '__main__':
    unittest.main()