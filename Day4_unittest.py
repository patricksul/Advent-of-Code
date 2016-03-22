sh ! /usr/bin/env python

import unittest

from Day4 import md5_calc

class Test_Day04(unittest.TestCase):
    
    def test_Example(self):
        self.assertEqual(md5_calc('abcdef','00000'),609043)
        self.assertEqual(md5_calc('pqrstuv','00000'),1048970)

    def test_Part_One(self):
        self.assertEqual(md5_calc('yzbqklnj','00000'),282749)

    def test_Part_Two(self):
        self.assertEqual(md5_calc('yzbqklnj','000000'),9962624)


if __name__ == '__main__':
    unittest.main()
