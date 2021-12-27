#PY:Chat GUI Sever 4.1

#pip install better_profanity

from better_profanity import profanity
import threading
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "192.168.0.33" 
PORT = 8000
my_socket.bind((ADDRESS, PORT))
my_socket.listen()

password = ""
 
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
            message = profanity.censor(message)
            if message == "/ping":
                client.send(f'Server : Hello {nickname}'.encode('ascii'))
            elif message == "/info":
                client.send(f'IP : {client} Nickname : {nickname}'.encode('ascii'))                       
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

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
