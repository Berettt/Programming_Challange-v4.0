from pyexpat.errors import messages
import socket, threading
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 55556))
server.listen()


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        thread = threading.Thread(target=messanges, args=(client,))
        thread.start()

def messanges(client):
    while True:
        messange = client.recv(1024).decode('ascii')
        print(messange)

receive()
