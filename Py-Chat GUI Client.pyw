#https://www.dummies.com/programming/python/using-tkinter-widgets-in-python/
from tkinter import *
from tkinter import simpledialog
import socket
import threading
import keyboard

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" 
port = 8000
my_socket.connect((host, port))

root = Tk()
root.title('Py:Chat Client')

nickname = "Guest"
nickname = simpledialog.askstring("Input", "Enter Username", parent=root)

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
    elif button_message == "/nickname":
        list1.insert(END,"Command not available")
        #nickname = simpledialog.askstring("Input", "Enter Username", parent=root)
    else:
        e.delete(0,END)
        socket_message = nickname + " : " + button_message
        my_socket.send(socket_message.encode())

e = Entry(root, width=50)
e.grid(row=2,column=1)

button1 = Button(root, text="Send", command=thread_sending)
button1.grid(row=2,column=2)

list1 = Listbox(root, width=55, height=20)
list1.grid(row=1,column=1, columnspan=2)

def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        list1.insert(END, message)

thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()

root.mainloop()