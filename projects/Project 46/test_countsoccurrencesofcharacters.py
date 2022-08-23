import unittest
import countsoccurrencesofcharacters

class test_Count_occurrences(unittest.TestCase):

    def test_user_input(self):

        testC = countsoccurrencesofcharacters.Count_occurrences()
        testC.count()
        self.assertEqual(testC.user, 'word') #input user == 'word'
        self.assertEqual(testC.char, 'w') # input char == 'w'
    
    def test_count_numberofcharacters(self):

        testC = countsoccurrencesofcharacters.Count_occurrences()
        testC.count()
        self.assertEqual(testC.number,4) #word.count(i) == 4

    def test_count_coutning(self):

        testC = countsoccurrencesofcharacters.Count_occurrences()
        testC.count()
        
        #testC.user == 'word'
        #  testC.user.count('w')==1
        #  testC.user.count('o')==1
        #  testC.user.count('r')==1
        #  testC.user.count('d')==1

        self.assertEqual(
            f'{testC.user[0]} == {testC.user.count(testC.user[0])}',
            f'{testC.user[0]} == 1'
        )
        self.assertEqual(
            f'{testC.user[1]} == {testC.user.count(testC.user[1])}',
            f'{testC.user[1]} == 1'
        )
        self.assertEqual(
            f'{testC.user[2]} == {testC.user.count(testC.user[2])}',
            f'{testC.user[2]} == 1'
        )
        self.assertEqual(
            f'{testC.user[3]} == {testC.user.count(testC.user[3])}',
            f'{testC.user[3]} == 1'
        )

if __name__ == '__main__':
    unittest.main()
