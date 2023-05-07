#!/usr/bin/env python

from tensors import Matrix
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)


class TestMatrix(unittest.TestCase):
    matrixA = Matrix(
        [
            (1, 2, 3),
            (4, 5, 6)
        ]
    )

    def testGetDimensions(self):
        pass

    def testGetRow(self):
        self.assertEqual(self.matrixA.getRow(1), (4, 5, 6))

    def testGetColumn(self):
        self.assertEqual(self.matrixA.getColumn(2), (3, 6))

    # Test Addition of Matrices
    def testAdd(self):
        pass

    # Test Multiplication of Matrices
    def testMult(self):
        pass

    # Test String representation of Matrix
    def testStr(self):
        pass

if __name__ == '__main__':
    unittest.main()
