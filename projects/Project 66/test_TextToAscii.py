import unittest
from TextToBinary import Main

class test_1(unittest.TestCase):

    def test_covertToascii_G(self):

        #print G

        test_class = Main()
        test_class.covertToascii()

        self.assertEqual(test_class.text,'G')
        self.assertEqual(test_class.ascii[0],ord('G'))
        self.assertEqual(test_class.ascii[0],71)

        # 71 is 'G's ascii code

    def test_covertToascii_multiple(self):

        #print abcd

        test_class = Main()
        test_class.covertToascii()

        self.assertEqual(test_class.text,'abcd')
        self.assertEqual(test_class.ascii[0],ord('a'))
        self.assertEqual(test_class.ascii[1],ord('b'))
        self.assertEqual(test_class.ascii[2],ord('c'))
        self.assertEqual(test_class.ascii[3],ord('d'))
        self.assertEqual(test_class.ascii[0],97)
        self.assertEqual(test_class.ascii[1],98)
        self.assertEqual(test_class.ascii[2],99)
        self.assertEqual(test_class.ascii[3],100)


if __name__ == '__main__':
    unittest.main()