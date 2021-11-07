#PY:Chat Server 3.2

# Library Define
from math import trunc
from datetime import datetime
import os 
import socket
import threading

#Terminal Size
cmd = 'mode 37,50'
os.system(cmd)
os.system("title PY:Chat 3.2")

#Welcome message
print("-----------------------------------")
print("-----Welcome To PY:Chat Server-----")
print("-----Developed By BlockWorks123----")
print("-----------------------------------")

#Socket Connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDRESS = "192.168.0.33" 
PORT = 12345
broadcast_list = []
my_socket.bind((ADDRESS, PORT))

while True:
    command = input("]")
    if command == "/help":
        print("/help -- Shows all commands")
        print("/time -- Shows current time")
        print("/clear -- Clears terminal ")
        print("/shutdown -- Shutsdown the server")
    if command == "/shutdown":
        exit()
    if command == "/time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Time :",current_time)
    if command == "/clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---------------------------------")
        print("----Welcome To PY:Chat Server----")
        print("----Developed By BlockWorks123---")
        print("---------------------------------")
    else:
        for client in broadcast_list:
            try:
                client.send(command.encode())
            except:
                broadcast_list.remove(client)
                print("Client removed",client)
    
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

