# PY:Chat GUI Client 4.3.4
Client Commands
- /help --> Shows list of available commands
- /clear --> Clears console chat messages

Admin Commands
- /kick {member} --> Kicks selected Member
- /ban {member} --> Bans selected Member

                if nickname.upper() == "ADMIN":
                    if message.startswith('/kick'):     
                        print(message)
                        name_to_kick = message[6:]
                        print(name_to_kick)
                if message.startswith('/ban'):     
                        print(message)
                        name_to_ban = message[5:]
                        print(name_to_ban)