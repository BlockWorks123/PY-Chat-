#PY:Chat Client
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
port = 3000
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
            print("ez")
        if message_to_send == "/shutdown":
            exit()
        if message_to_send == "/help":
            print("/clear -- clears all messages")
            print("/help -- Shows all commands")
            print("/disconnect -- Disconnects client")
            print("/reconnect -- Reconnects Client")
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
        else:
            message_to_send = nickname + " : " + message_to_send
            my_socket.send(message_to_send.encode())

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
