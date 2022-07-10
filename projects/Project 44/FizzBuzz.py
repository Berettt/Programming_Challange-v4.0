
def main():
    welcome = int(input('Welcome to FizzBuzz, how many numbers you want to count? '))
    print()
    for f in range(welcome+1):
        if f%5==0 and f%3==0:
            print('FizzBuzz')
        elif f%3==0:
            print('Fizz')
        elif f%5==0:
            print('Buzz')
        else:
            print(f)
main()



