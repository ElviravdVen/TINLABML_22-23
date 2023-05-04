#!/usr/bin/env python

from tensors import Scalar
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class TestTensors(unittest.TestCase):

    # Test Addition of Scalars
    def testAdd(self):
        self.assertEqual(Scalar(1) + Scalar(-1), 0)

    def testMult(self):
        self.assertEqual(Scalar(0.5) * Scalar(2), 1)

    def testGetValue(self):
        self.assertEqual(Scalar(3.14).getValue(), 3.14)

if __name__ == '__main__':
    unittest.main()