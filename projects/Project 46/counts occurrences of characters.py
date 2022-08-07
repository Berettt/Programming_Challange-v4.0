class Count_occurrences:

    #input
    def user_input(self)->str:
        self.user = input('Type in a STRING: ')


    #count occurrences of input
    def count(self):
        print('String contains: ')
        for i in range(len(self.user)):
            self.occurrences = self.user.count(self.user[i])
            
            print(f'{self.user[i]} = {self.occurrences}')


C = Count_occurrences()
C.user_input()
C.count()
