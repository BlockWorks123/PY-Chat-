#PY:Chat GUI Sever 2.1

import socket
import threading
from typing import Tuple

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "127.0.0.1" 
PORT = 8000
my_socket.bind((ADDRESS, PORT))
my_socket.listen()
 
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        index = clients.index(client)
        nickname = nicknames[index]
        try:
            message = client.recv(1024)
            broadcast(f'{nickname} : {message}')
        except:
            
            clients.remove(client)
            client.close()
            
            broadcast(f'{nickname} Left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True: 
        client, address = my_socket.accept()
        print(f'Connected with {str(address)}')
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        #broadcast(f'{nickname} Joined the chat'.encode('ascii'))
        client.send(f'{nickname} joined the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()