import unittest
import average

class Testcase(unittest.TestCase):
    def testOne(self):
        typeList = type(average.randomList(10))
        if self.assertEqual(typeList,type([])):
            print("Fuction does not generate a list")
        else:
            print("Fuction does generate a list")

    def testTwo(self):
        '''TESTING LIST IS NOT EMPTY'''
        self.assertNotEqual(average.randomList(10),[])

    def testThree(self):
        '''CHECKING THAT THE LIST DOES NOT HAVE A LENGTH OF 0'''
        self.assertNotEqual(average.getListLen(),0)


if __name__ == '__main__':
    unittest.main()
