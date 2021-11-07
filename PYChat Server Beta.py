
#Libary Define
import socket
import threading
import os
from datetime import datetime 
from math import trunc

#Terminal Size
cmd = 'mode 37,50'
os.system(cmd)
os.system("title PY:Chat 4.0")

#Welcome message
print("-----------------------------------")
print("-----Welcome To PY:Chat Server-----")
print("-----Developed By BlockWorks123----")
print("-----------------------------------")

#Command Console
while True:
    command = input("]")
    if command == "/help":
        print("/help -- Shows all commands")
        print("/time -- Shows current time")
        print("/clear -- Clears terminal ")
        print("/shutdown -- Shutsdown the server")