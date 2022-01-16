#PY:Chat Server 5.0

#pip install better_profanity

from better_profanity import profanity
import threading
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "192.168.0.33"
PORT = 8000
my_socket.bind((ADDRESS, PORT))
my_socket.listen()

clients = []
nicknames = []

def broadcast(message_send):
    for client in clients:
        client.send(message_send)

def handle(client,address):
    index = clients.index(client)
    nickname = nicknames[index]
    while True:
        try:
            message = client.recv(1024).decode()
            message = profanity.censor(message)
            if message.startswith('/'):
                if message.startswith('/info'):
                    client.send(f'IP : {address} Client : {nickname}'.encode('ascii'))
                elif message.startswith('/ping'):
                    client.send(f'Server : Hello {nickname}'.encode('ascii'))
                elif message.startswith('/broadcast'):
                    if nickname == "ADMIN":
                        command_arg = message.replace('/broadcast ','')
                        tell_all(command_arg)
                    else:
                        client.send(f'You do not have permissions for that command'.encode('ascii'))               
                elif message.startswith('/kick'):
                    if nickname == "ADMIN":
                        print('Test Kick')
                        command_arg = message.replace('/kick ','')
                        kick_user(command_arg)
                    else:
                        client.send(f'You do not have permissions for that command'.encode('ascii'))
                else:                       
                    client.send(f'{message} is not a valid command'.encode('ascii'))
            else:    
                broadcast(f'{nickname} : {message}'.encode('ascii'))
                print(f'{nickname} : {message}')
        except:
            if client in clients:
                clients.remove(client)
                client.close()
                broadcast(f'{nickname} Left the chat!'.encode('ascii'))
                nicknames.remove(nickname)
                break

def tell_all(message_tell):
    for client in clients:
        client.send('%BROADCAST%'.encode('ascii'))
        client.send(message_tell.encode('ascii'))

def receive():
    while True: 
        client, address = my_socket.accept()
        print(f'Connected with {str(address)}')
    
        client.send('%NICKNAME%'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        
        if nickname == "ADMIN":
            client.send('%PASSWORD%'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            if password != "Password":
                client.send('%REFUSE%'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} Joined the chat'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,address))
        thread.start()

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('%KICK%'.encode('ascii'))
        client_to_kick.close()    
        nicknames.remove(name)
        broadcast(f'{name} was kicked by a ADMIN'.encode('ascii'))

print("Server is listening...")
receive()