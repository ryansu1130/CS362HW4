import unittest
import cube
import math

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(cube.cubeV(5,5,5),125)

    def testTwo(self):
        self.assertEqual(cube.cubeV(pow(2,2),pow(4,4),pow(1,1)),1024)

    def testThree(self):
        '''Can Not Use Negative Numbers'''
        self.assertNotEqual(cube.cubeV(-5,-5,5),125)


if __name__ == '__main__':
    unittest.main()
