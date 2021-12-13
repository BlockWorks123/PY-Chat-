#PY:Chat GUI Client 1.2.1

from tkinter import *
import threading
import socket
import os

server_host = "127.0.0.1"
#Client
def client_host(server_host):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    host = server_host
    my_socket.connect((host, port))

    nickname = "James"

    root = Tk()
    root.title('Py:Chat Client')

    def thread_sending():
        button_message = e.get()
        if button_message == "/clear":
            list1.delete(0,END)
            e.delete(0,END)
        elif button_message == "/help":
            list1.insert(END,"/help -- Shows list of commands")
            list1.insert(END,"/clear -- Clears console")
            list1.insert(END,"/shutdown -- Shutsdown PY:Chat")
            list1.insert(END,"/nickname -- Changes nickname")
        elif button_message == "/shutdown":
            exit()
        else:
            e.delete(0,END)
            socket_message = nickname + " : " + button_message
            my_socket.send(socket_message.encode())

    e = Entry(root, width=50)
    e.grid(row=3,column=1)

    button1 = Button(root, text="Send", command=thread_sending)
    button1.grid(row=3,column=2)

    list1 = Listbox(root, width=55, height=20)
    list1.grid(row=2,column=1,columnspan=2)

    def run_server():
        print("hi")
        os.system('Py-Chat GUI Server.py')

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    
    filemenu.add_command(label="Run Server", command=run_server)
    menubar.add_cascade(label="Server", menu=filemenu)


    def thread_receiving():
        while True:
            message = my_socket.recv(1024).decode()
            list1.insert(END, message)
    
    thread_send = threading.Thread(target=thread_sending)
    thread_receive = threading.Thread(target=thread_receiving)
    thread_send.start()
    thread_receive.start()

    root.config(menu=menubar)
    root.mainloop()

client_host()

'''
#Launcher
def start_client():
    nameEntry.delete(0,END)
    ipEntry.delete(0,END)
    client_host()
    first.quit()

first = Tk()  
first.title('PY:Chat Launcher')

nameLabel = Label(first, text="Name: ")
nameLabel.grid(row=0, column=0)
nameEntry = Entry(first, width=25)
nameEntry.grid(row=0, column=1)  

ipLabel = Label(first,text="Address:")
ipLabel.grid(row=1, column=0)  
ipEntry = Entry(first, width=25)
ipEntry.grid(row=1, column=1)  

loginButton = Button(first, text="Login", command=start_client).grid(row=4, column=0)  

first.mainloop()
'''