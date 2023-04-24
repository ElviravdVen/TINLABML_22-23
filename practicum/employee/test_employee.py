#!/usr/bin/env python

from employee import Employee
import logging
import unittest

logging.basicConfig(level=logging.INFO)



class TestEmployee(unittest.TestCase):
    
    def __init__(self):
        self.employee1 = Employee("Hans", "O", 5000)
        self.employee2 = Employee("Hans", "W", 4800, 1200)

    # unit test
    def testGetFullName(self):
        hansen = list()
        logging.info(self.assertEqual(self.employee1.getFullName(), "Hans O"))
        self.assertEqual(self.employee2.getFullName(), "Hans A")s

    # unit test
    def testMoreThanMe(self, other):
        self.assertGreater

if __name__ == "__main__":
    unittest.main()
