import unittest
from TextToBinary import Main

class test_1(unittest.TestCase):

    def test_convertTobinary_singleword(self):

        test_class = Main()
        test_class.covertToascii()
        test_class.convertTobinary()

        # print G

        #1000111 is "G"'s binary code
        self.assertEqual(test_class.binary[0],'1000111')

class test_2(unittest.TestCase):

    def test_convertTobinary_multiplewords(self):

        test_class = Main()
        test_class.covertToascii()
        test_class.convertTobinary()

        # print abcd

        self.assertEqual(test_class.binary[0],'1100001')
        self.assertEqual(test_class.binary[1],'1100010')
        self.assertEqual(test_class.binary[2],'1100011')
        self.assertEqual(test_class.binary[3],'1100100')

    
if __name__ == '__main__':
    unittest.main()