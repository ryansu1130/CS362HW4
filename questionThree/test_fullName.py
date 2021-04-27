import unittest
import fullName

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fullName.genFullName("Ryan","Su"), "Ryan Su")

    def testTwo(self):
        s = type(fullName.genFullName("Ryan","Su"))
        self.assertEqual(s, type(""))

    def testThree(self):
        self.assertEqual(fullName.genFullName("1Ryan","Su"), "Ryan Su")

if __name__ == '__main__':
    unittest.main()
