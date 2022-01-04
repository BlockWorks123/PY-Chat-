#PY:Chat GUI Client 4.6.2

from tkinter import *
from tkinter import messagebox
import threading
import socket
import time

stop_thread = False

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
    root.title(f'PY:Chat Client - Nickname : {nickname}')

    #Password 
    def password_promt():
        password_tk = Tk()  
        password_tk.title('PY:Chat')

        passLabel = Label(password_tk, text="Password: ")
        passLabel.grid(row=0, column=0)
        passEntry = Entry(password_tk, width=28, show="*")
        passEntry.grid(row=0, column=1)  

        def give_password():
            password = passEntry.get()
            my_socket.send(password.encode('ascii'))
            password_tk.destroy()

        loginButton = Button(password_tk, text="Login", command=give_password)
        loginButton.grid(row=4, column=0, columnspan=2)

        password_tk.mainloop()
    
    def thread_sending():
        button_message = e.get()
        if button_message.startswith('/'):
            if button_message.startswith('/help'):
                list1.insert(END, '/help --> Shows list of available commands')
                list1.insert(END, '/clear --> Clears console chat messages')
                list1.insert(END, '/info --> Shows IP and Nickname of Client')
                list1.insert(END, '/ping --> Pings server')
            elif button_message == "/clear":
                list1.delete(0,END)
            else:
                my_socket.send(button_message.encode())
        else:
            my_socket.send(button_message.encode())
        e.delete(0,END)

    def thread_receiving():
        while True:
            try:
                message = my_socket.recv(1024).decode('ascii')
                if message == "%KICK%":
                    messagebox.showwarning("Connection Aborted", "Client was kicked by Admin")
                elif message == "%BAN%":
                    stop_thread = True
                    if messagebox.showerror("Connection Refused", "You are banned from this Server"):
                        exit()
                elif message == "%BROADCAST%":
                    broadcast_message = my_socket.recv(1024).decode('ascii')
                    messagebox.showinfo("Broadcast", broadcast_message)
                elif message == "%NICKNAME%":
                    my_socket.send(nickname.encode('ascii'))
                    next_message = my_socket.recv(1024).decode('ascii')
                    if next_message == "%PASSWORD%":
                        password_promt()
                        if my_socket.recv(1024).decode('ascii') == '%REFUSE%':
                            stop_thread = True
                            if messagebox.showwarning("Connection Refused", "Incorrect password Entered"):               
                                exit()
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
    list1.insert(END, f'{nickname} Joined the chat')

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

ipEntry.insert(0,"172.16.112.130")

loginButton = Button(first, text="Login", command=start_client)
loginButton.grid(row=4, column=0,columnspan=2)  

first.mainloop()