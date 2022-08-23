class Count_occurrences:

    #input
    def user_input(self)->str:
        self.user = input('Type in a STRING: ')
        print('Type in a certain character of string ')
        print('If you want to count all occurrences just press enter ')
        self.char = input('--> ')


    #count occurrences of input
    def count(self):
        self.user_input()
        print('String contains: ')

        for i in range(len(self.user)):
            if self.char == '':
                print(f'{self.user[i]} == {self.user.count(self.user[i])}')
        print(f'Number of characters: {i+1} ')
        if self.char != '':
            print(f"Certain character: '{self.char}' : {self.user.count(self.char)} ")


def Countoccurrences():
    C = Count_occurrences()
    C.count()

if __name__ == '__main__':
    Countoccurrences()
