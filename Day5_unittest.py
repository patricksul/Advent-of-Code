#! /usr/bin/env python

import unittest

from Day5 import nice_string 

class Test_Day05(unittest.TestCase):

    def test_Example1(self):
        self.assertEqual(nice_string('ugknbfddgicrmopn'),True)
    def test_Example2(self):
        self.assertEqual(nice_string('aaa'),True)
    def test_Example3(self):
        self.assertEqual(nice_string('jchzalrnumimnmhp'),True)
    def test_Example4(self):
        self.assertEqual(nice_string('haegwjzuvuyypxyu'),True)
    def test_Example5(self):
        self.assertEqual(nice_string('dvszwmarrgswjxmb'),True)

    def test_Part_One(self):
        self.assertEqual(nice_string(open('Day5_input.txt','r')),True)



if __name__ == '__main__':
    unittest.main()

