#PY:Chat GUI Client 1.1

from tkinter import *
from tkinter import simpledialog
import socket
import threading
import keyboard

#Client
def client_host():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    host = "127.0.0.1"
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

    def donothing():
        print("hi")

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    e = Entry(root, width=50)
    e.grid(row=3,column=1)

    button1 = Button(root, text="Send", command=thread_sending)
    button1.grid(row=3,column=2)

    list1 = Listbox(root, width=55, height=20)
    list1.grid(row=2,column=1,columnspan=2)

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