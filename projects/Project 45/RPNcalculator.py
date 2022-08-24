class RPN():
    def welcome(self):
        print('REVERSE POLISH NOTATION')
        print('-----------------------')
        print()

    
    def algorithm(self):

        self.sztos = [] #sztos == stack
        self.array = []

        while True:
            print('Type in "f" for finishing an equation')
            self.in_put = input('RPN Calculator: ')

            if self.in_put == '+':
                # stock technique
                self.dodaj = int(self.sztos[-2]) + int(self.sztos[-1])
                self.array.append(self.in_put)
                self.array.append(self.dodaj)
                self.sztos.remove(self.sztos[-2])
                self.sztos.remove(self.sztos[-1])
                self.sztos.append(self.dodaj)

            elif self.in_put == '-':
                self.dodaj = int(self.sztos[-2]) - int(self.sztos[-1])
                self.array.append(self.in_put)
                self.array.append(self.dodaj)
                self.sztos.remove(self.sztos[-2])
                self.sztos.remove(self.sztos[-1])
                self.sztos.append(self.dodaj)

            elif self.in_put == '*':
                self.dodaj = int(self.sztos[-2]) * int(self.sztos[-1])
                self.array.append(self.in_put)
                self.array.append(self.dodaj)
                self.sztos.remove(self.sztos[-2])
                self.sztos.remove(self.sztos[-1])
                self.sztos.append(self.dodaj)

            elif self.in_put == '/':
                self.dodaj = int(self.sztos[-2]) / int(self.sztos[-1])
                self.array.append(self.in_put)
                self.array.append(self.dodaj)
                self.sztos.remove(self.sztos[-2])
                self.sztos.remove(self.sztos[-1])
                self.sztos.append(self.dodaj)

            elif self.in_put == 'f':
                print(f'Stack: {self.sztos}')
                print(f'The result is: {self.sztos[-1]}')
                break 

            else: #numbers
                self.sztos.append(self.in_put)
                self.array.append(self.in_put)


if __name__ == "__main__":
    Calculator = RPN()
    Calculator.welcome()
    Calculator.algorithm()
