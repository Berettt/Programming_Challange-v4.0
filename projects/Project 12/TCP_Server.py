import socket
import threading


host = '127.0.0.1'
port = 55555
serwer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serwer.bind((host,port))
serwer.listen()
clients = []
nicks = []

def send_messanges(mess):
    for i in clients:    
        i.send(mess)

def messanges(client):

    while True:
        try: #send mess
            messange = client.recv(1024)
            send_messanges(messange)
        except:  #terminate and exit all
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            send_messanges('{} left!'.format(nickname).encode('ascii'))
            nicks.remove(nickname)

def main_sever_function():
    while True:
        klient, adres = serwer.accept()

        print('Connected with {}'.format(str(adres)))

        klient.send('TEST'.encode('ascii'))

        nickname = klient.recv(1024).decode('ascii')

        nicks.append(nickname)
        clients.append(klient)

        print('nickname is {}'.format(nickname))
        send_messanges("{} just joined!".format(nickname).encode('ascii'))
        klient.send('Connected to chat!'.encode('ascii'))


        thread = threading.Thread(target=messanges,args=(klient,))
        thread.start()
        
print('Server is on!')
main_sever_function()