import socket, sys, threading

Nickname = input('Enter your nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def welcome(nick):
    print(f'Hello {nick}')
    try:
        client.connect(('127.0.0.1', 55556))
        print('You are connected to the server successfully')
    except:
        print('Cant connect to the server')

def login(nick,channel):
    notification_login_mess = f'{nick} just joined the {channel} !'

    print(notification_login_mess)

def user_input():
    while True:

        mes = input(">> ")
        if mes == 'exit':
            sys.exit()
        client.send(mes.encode('ascii'))
        

def main():
    welcome(Nickname)
    receive_thread = threading.Thread(target=user_input)
    receive_thread.start()


if __name__ == "__main__":
    main()


