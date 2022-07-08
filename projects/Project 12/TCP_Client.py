import socket
import threading

nick = input('Type in your nickname: ')

host = '127.0.0.1'
port = 55555
klient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klient.connect((host, port))

def sending_messages():
    while True:
        message = '{}: {}'.format(nick, input(''))
        klient.send(message.encode('ascii'))

def main():
    while True:
        try:
            message = klient.recv(1024).decode('ascii')
            if message == 'TEST':
                klient.send(nick.encode('ascii'))
            else:
                print(message)
        except:
            klient.close()
            break

receive_thread = threading.Thread(target=main)
receive_thread.start()

write_thread = threading.Thread(target=sending_messages)
write_thread.start()