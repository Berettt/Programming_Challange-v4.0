import unittest
import RPNcalculator

class test_rpn_1(unittest.TestCase):

    def test_rpn_add(self):

        testrpnadd = RPNcalculator.RPN()
        testrpnadd.algorithm()

        #2 4 6 8 10 + + + + == 30
        #result
        self.assertEqual(testrpnadd.sztos[-1],30)


class test_rpn_2(unittest.TestCase):
    def test_rpn_sub(self):

        testrpnsub = RPNcalculator.RPN()
        testrpnsub.algorithm()

        # 100 50 - -20 == 50
        self.assertEqual(testrpnsub.sztos[-1],50)


class test_rpn_3(unittest.TestCase):
    def test_rpn_mul(self):

        testrpnmul = RPNcalculator.RPN()
        testrpnmul.algorithm()

        # 5 10 * 20 * == 1000
        self.assertEqual(testrpnmul.sztos[-1],1000)


class test_rpn_4(unittest.TestCase):
    def test_rpn_div(self):

        testrpndiv = RPNcalculator.RPN()
        testrpndiv.algorithm()

        # 500 5 / 10  / == 10
        self.assertAlmostEqual(testrpndiv.sztos[-1],10)

class test_rpn_5(unittest.TestCase):
    def test_rpn_mix(self):

        testrpnmix = RPNcalculator.RPN()
        testrpnmix.algorithm()

        # 12 2 3 4 * 10 5 / + * + == 40
        self.assertAlmostEqual(testrpnmix.sztos[-1],40)

if __name__ == '__main__':
    unittest.main()