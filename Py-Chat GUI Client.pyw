#PY:Chat GUI Client 4.2

from tkinter import *
import threading
import socket

#Client
def client_host():
    nickname = nameEntry.get()
    host = ipEntry.get()
    nameEntry.delete(0,END)
    ipEntry.delete(0,END)
    
    if host == "":
        host = "127.0.0.1"

    first.destroy()

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    my_socket.connect((host, port))

    root = Tk()
    root.title('Py:Chat Client')

    def thread_sending():
        button_message = e.get()
        if button_message == "/help":
            list1.insert(END, '/help --> Shows list of available commands')
            list1.insert(END, '/clear --> Clears console chat messages')
            list1.insert(END, '/info --> Shows IP and Nickname of Client')
        elif button_message == "/clear":
            list1.delete(0,END)
        else:
            my_socket.send(button_message.encode())
        e.delete(0,END)

    def thread_receiving():
        while True:
            try:
                message = my_socket.recv(1024).decode('ascii')
                if message == "%nickname%":
                    my_socket.send(nickname.encode('ascii'))
                    next_message = my_socket.recv(1024).decode('ascii')
                    if next_message == "%password%":
                        return
                else:
                    list1.insert(END, message)
            except:
                my_socket.close()
                break


    e = Entry(root, width=50)
    e.grid(row=3,column=1)
    
    button1 = Button(root, text="Send", command=thread_sending)
    button1.grid(row=3,column=2)
    
    list1 = Listbox(root, width=55, height=20)
    list1.grid(row=2,column=1,columnspan=2)

    thread_send = threading.Thread(target=thread_sending)
    thread_receive = threading.Thread(target=thread_receiving)
    thread_send.start()
    thread_receive.start()

    root.mainloop()

#Launcher
def start_client():
    client_host()

first = Tk()  
first.title('PY:Chat')

nameLabel = Label(first, text="Name: ")
nameLabel.grid(row=0, column=0)
nameEntry = Entry(first, width=28)
nameEntry.grid(row=0, column=1)  

ipLabel = Label(first,text="Address:")
ipLabel.grid(row=1, column=0)  
ipEntry = Entry(first, width=28)
ipEntry.grid(row=1, column=1)

ipEntry.insert(0,"192.168.0.33")

loginButton = Button(first, text="Login", command=start_client)
loginButton.grid(row=4, column=0,columnspan=2)  

first.mainloop()
