
def main():

    alphabet = [
            'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    betabet =  [
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    encrypt = []

    code = input('Encrypt messange: ')

    for a in range(len(code)):
        
        if code[a] in alphabet and code[a].isupper():
            if code[a] == alphabet[0]:
                print(alphabet[13],end='')
            if code[a] == alphabet[1]:
                print(alphabet[14],end='')
            if code[a] == alphabet[2]:
                print(alphabet[15],end='')
            if code[a] == alphabet[3]:
                print(alphabet[16],end='')
            if code[a] == alphabet[4]:
                print(alphabet[17],end='')
            if code[a] == alphabet[5]:
                print(alphabet[18],end='')
            if code[a] == alphabet[6]:
                print(alphabet[19],end='')
            if code[a] == alphabet[7]:
                print(alphabet[20],end='')
            if code[a] == alphabet[8]:
                print(alphabet[21],end='')
            if code[a] == alphabet[9]:
                print(alphabet[22],end='')
            if code[a] == alphabet[10]:
                print(alphabet[23],end='')
            if code[a] == alphabet[11]:
                print(alphabet[24],end='')
            if code[a] == alphabet[12]:
                print(alphabet[25],end='')
            if code[a] == alphabet[25]:
                print(alphabet[25-13],end='')
            if code[a] == alphabet[24]:
                print(alphabet[24-13],end='')
            if code[a] == alphabet[23]:
                print(alphabet[23-13],end='')
            if code[a] == alphabet[22]:
                print(alphabet[22-13],end='')
            if code[a] == alphabet[21]:
                print(alphabet[21-13],end='')
            if code[a] == alphabet[20]:
                print(alphabet[20-13],end='')
            if code[a] == alphabet[19]:
                print(alphabet[19-13],end='')
            if code[a] == alphabet[18]:
                print(alphabet[18-13],end='')
            if code[a] == alphabet[17]:
                print(alphabet[17-13],end='')
            if code[a] == alphabet[16]:
                print(alphabet[16-13],end='')
            if code[a] == alphabet[15]:
                print(alphabet[15-13],end='')
            if code[a] == alphabet[14]:
                print(alphabet[14-13],end='')
            if code[a] == alphabet[13]:
                print(alphabet[0],end='')

        elif code[a] in betabet and code[a].islower():
            if code[a] == betabet[0]:
                print(betabet[13],end='')
            if code[a] == betabet[1]:
                print(betabet[14],end='')
            if code[a] == betabet[2]:
                print(betabet[15],end='')
            if code[a] == betabet[3]:
                print(betabet[16],end='')
            if code[a] == betabet[4]:
                print(betabet[17],end='')
            if code[a] == betabet[5]:
                print(betabet[18],end='')
            if code[a] == betabet[6]:
                print(betabet[19],end='')
            if code[a] == betabet[7]:
                print(betabet[20],end='')
            if code[a] == betabet[8]:
                print(betabet[21],end='')
            if code[a] == betabet[9]:
                print(betabet[22],end='')
            if code[a] == betabet[10]:
                print(betabet[23],end='')
            if code[a] == betabet[11]:
                print(betabet[24],end='')
            if code[a] == betabet[12]:
                print(betabet[25],end='')
            if code[a] == betabet[25]:
                print(betabet[25-13],end='')
            if code[a] == betabet[24]:
                print(betabet[24-13],end='')
            if code[a] == betabet[23]:
                print(betabet[23-13],end='')
            if code[a] == betabet[22]:
                print(betabet[22-13],end='')
            if code[a] == betabet[21]:
                print(betabet[21-13],end='')
            if code[a] == betabet[20]:
                print(betabet[20-13],end='')
            if code[a] == betabet[19]:
                print(betabet[19-13],end='')
            if code[a] == betabet[18]:
                print(betabet[18-13],end='')
            if code[a] == betabet[17]:
                print(betabet[17-13],end='')
            if code[a] == betabet[16]:
                print(betabet[16-13],end='')
            if code[a] == betabet[15]:
                print(betabet[15-13],end='')
            if code[a] == betabet[14]:
                print(betabet[14-13],end='')
            if code[a] == betabet[13]:
                print(betabet[0],end='')
        else:
            print(' ',end='')


main()