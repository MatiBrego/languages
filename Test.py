import unittest

import classReader
import os

class MyTestCase(unittest.TestCase):


    def test_number_of_directorys(self):

        file = open(r"C:\Users\Agust\PycharmProjects\languages\testDir\dir1\testFile1.py")
        result = classReader.readFile(r"C:\Users\Agust\PycharmProjects\languages\testDir\dir1\testFile1.py")

        self.assertEqual(result[0].methodQty(),3)
        self.assertEqual(result[0].getCls(), "person")
        self.assertEqual(result[1].getCls(), "car")
        self.assertEqual(result[2].methodQty(), 1)





