# PY:Chat - Client & Server 3.1.6

Client Commands
- /clear - Clears terminal 
- /help - Shows list of commands
- /shutdown - Closes application
- /disconnect = Disconnects client
- /reconnect - Reconnects client
- /time - Shows current time
- /address - Shows selected address

Server Commands
- /clear - Clears terminal
- /help - Shows list of commands
- /time - Shows current time
- /shutdown - Shutsdown the server
- 

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
