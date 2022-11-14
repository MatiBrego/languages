import unittest

import classReader
import os

import pyFilesReader


class MyTestCase(unittest.TestCase):


    def test_number_of_methods(self):

        file = open(r"testDir/dir1/testFile1.py")
        result = classReader.readFile(r"testDir\dir1\testFile1.py")


        self.assertEqual(result[0].methodQty(),3)
        self.assertEqual(result[0].getCls(), "person")
        self.assertEqual(result[1].getCls(), "car")
        self.assertEqual(result[2].methodQty(), 1)

    def test_number_of_directories(self):
        file = open(r"testDir/dir1/testFile1.py")

        self.assertEqual(pyFilesReader.getAllFilePaths(dir="testDir", filePaths=[]), 3)
        #This assertEqual tests if the amount of directories is equal to 2


    def test_paths_are_updated_correctly(self):
        file = open(r"testDir/dir1/testFile1.py")
        filePaths = []
        pyFilesReader.getAllFilePaths(dir="testDir", filePaths=filePaths)

        self.assertEqual(filePaths[0], "testDir\\dir1\\testFile1.py")
        self.assertEqual(filePaths[1], "testDir\\dir2\\testFile2.1.py")


    def test_amt_of_classes(self):
        file = open(r"testDir/dir1/testFile1.py")
        result = classReader.readFile(r"testDir\dir1\testFile1.py")
        qty_of_classes = 0


        for res in result:
            if(res.getCls()!= None):
                qty_of_classes+=1
        self.assertEqual(qty_of_classes,2)
