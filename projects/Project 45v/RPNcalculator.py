class RPN():
    def welcome(self):
        print('simple REVERSE POLISH NOTATION')
        print('-----------------------')
        print()

    def __init__(self) -> None:
        pass

    def algorithm(self):
        self.sztos = []
        self.wyniki = []
        self.wynikisztos = []
        while True:
            self.in_put = input('Type in numbers or operators: ')

            if self.in_put == '+':

                self.wynik = int(self.wynikisztos[-2]) + int(self.wynikisztos[-1])
                self.wynikisztos.append(self.wynik)

            elif self.in_put == '-':

                self.wynik = int(self.wynikisztos[-2]) - int(self.wynikisztos[-1])
                
                self.wynikisztos.append(self.wynik)

            elif self.in_put == '*':

                self.wynik = int(self.wynikisztos[-2]) * int(self.wynikisztos[-1])
                self.wynikisztos.append(self.wynik)

            elif self.in_put == '/':

                self.wynik = int(self.wynikisztos[-2]) / int(self.wynikisztos[-1])
                self.wynikisztos.append(self.wynik)
            
            elif self.in_put == 'w':
                print(self.wynikisztos[-1])
                break 


            elif self.in_put == 'b':
                break
            else: #numbers
                self.sztos.append(self.in_put)
                self.wynikisztos.append(self.in_put)
                

    def __str__(self) -> str:
        pass



Calculator = RPN()
Calculator.welcome()
Calculator.algorithm()
