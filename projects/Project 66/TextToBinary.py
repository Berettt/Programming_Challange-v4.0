class Main:

    def __init__(self):

        self.text = input('Type in text and I will translate it into binary code: ')

    def covertToascii(self):

        self.ascii = []

        for n in range(len(self.text)):

            text = self.text[n]
            convert = ord(text)
            self.ascii.append(convert)

    def convertTobinary(self):

        self.binary = []

        for m in range(len(self.ascii)):

            convert = bin(self.ascii[m])

            self.binary.append(convert[2:])

    def output(self) -> str:

        print_input = self.text        
        print_output = self.binary

        print()
        print( f'Your binary code for "{print_input}" --> ',end='')
        print(*print_output,end='')


def start():

    Program = Main()
    Program.covertToascii()
    Program.convertTobinary()
    Program.output()

if __name__ == '__main__':
    start()