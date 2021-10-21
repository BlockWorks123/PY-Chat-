#Library Define
import os
import socket
import threading

#Welcome Message
print("-----------------------------------")
print("-----Welcome to PY:Chat Client-----")
print("-----Developed By BlockWorks123----")
print("-----------------------------------")

#Socket Connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.1.1"
port = 8000
my_socket.connect((host, port))

#Nickname Input
nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

#Message Sending
def thread_sending():
    while True:
        message_to_send = input("")
        if message_to_send == "/help":
            print("/clear -- clears all messages")
            print("")
        if message_to_send == "/clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            message_to_send = nickname + " : " + message_to_send
        my_socket.send(message_to_send.encode())

#Message Receiving
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        

#Thread Define
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
