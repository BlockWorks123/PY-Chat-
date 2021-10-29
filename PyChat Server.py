#PY:Chat Server

#Library Define
import socket
import threading
#Welcome message
print("---------------------------------")
print("----Welcome To PY:Chat Server----")
print("----Developed By BlockWorks123---")
print("---------------------------------")

#Socket Connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "192.168.0.33" 
PORT = 12345
broadcast_list = []
my_socket.bind((ADDRESS, PORT))

#Command line
while True:
    command = input("]")
    if command == "/help":
        print("/help -- Shows all commands")

#Socket listening for message
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
        message = client.recv(1024).decode()
        if message:
            print("Client Message>",message)
            broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return
#Server "client diconnect" message
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print("Client removed",client)
accept_loop()