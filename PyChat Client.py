#PY:Chat Client

#Library Define
import random
from datetime import datetime
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
host = "192.168.0.33" 
port = 12345
my_socket.connect((host, port))

#Nickname Input
nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

#Message Sending
def thread_sending():
    while True:
        message_to_send = input("]")
        if message_to_send == "ez":
            letters = ['PY:Chat is the best', 'Person 1: Whatsapp Person 2: What app?', 'Discord or Disstrack', 'BlockWorks123 who is that?', '2005 Person: Do you wana chat on Skype', 'Student: Why do we have to use teams?']
            random_index = random.randint(0,len(letters)-1)
            my_socket.send(random_index.encode())
            print(letters[random_index])
        if message_to_send == "/time":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Time:",current_time)
        if message_to_send == "/shutdown":
            exit()
        if message_to_send == "/help":
            print("/clear -- clears all messages")
            print("/help -- Shows all commands")
            print("/disconnect -- Disconnects client")
            print("/reconnect -- Reconnects Client")
            print("/shutdown -- Closes application")
            print("/time -- Shows current time")
            print("/address -- Shows selected address")
        if message_to_send == "/reconnect":
            print("Command not available")
            # my_socket.connect((host, port))
        if message_to_send == "/disconnect":
            print("Command not available")
            #my_socket.shutdown(2)    # 0 = done receiving, 1 = done sending, 2 = both
        if message_to_send == "/clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-----------------------------------")
            print("-----Welcome to PY:Chat Client-----")
            print("-----Developed By BlockWorks123----")
            print("-----------------------------------")
        if message_to_send == "/address":
            print("Address :", host)
        if message_to_send == "/nickname":
            print("Nickname : ",nickname)
        else:
            message_to_send = nickname + " : " + message_to_send
            my_socket.send(message_to_send.encode())
            #normal message

#Message Receiving
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        msg = message.find(nickname)
        if msg == 0:
            return           
        else:
            print(message)

#Thread Define
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
