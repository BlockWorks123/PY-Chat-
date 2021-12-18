#PY:Chat GUI Sever 3.1.2

import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "127.0.0.1" 
PORT = 8000
broadcast_list = []
my_socket.bind((ADDRESS, PORT))

def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)

#Socket listening for nickname     
def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,) #the list of argument for the function
        )
    client_thread.start()

#Client message receiver and broadcaster
def listen_thread(client):
    while True:
        print(broadcast_list)
        message = client.recv(1024).decode()
        if message:
            print("Client Message>",message)
            broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return
#Server "client diconnect" message
def broadcast(message):
    socket_client = socket.gethostname()
    ip_socket_client = socket.gethostbyname(socket_client)
    print(ip_socket_client)
    print(socket_client)
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print("Client removed",client)
accept_loop()      

