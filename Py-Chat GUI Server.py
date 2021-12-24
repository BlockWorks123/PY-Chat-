#PY:Chat GUI Sever 3.4.1

import threading
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "127.0.0.1" 
PORT = 8000
my_socket.bind((ADDRESS, PORT))
my_socket.listen()
 
clients = []
nicknames = []

def broadcast(message_send):
    for client in clients:
        client.send(message_send)

def handle(client):
    index = clients.index(client)
    nickname = nicknames[index]
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "/ping":
                client.send(f'Hello {nickname}'.encode('ascii'))           
            else:    
                broadcast(f'{nickname} : {message}'.encode('ascii'))
                print(message)
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
    
        client.send('%nickname%'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} Joined the chat'.encode('ascii'))
        #client.send(f'{nickname} joined the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()