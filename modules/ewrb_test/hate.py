import wrbcommands, send

def hating(SENDER,MESSAGE,CMD):
    send.send('HATE!!!')

# Next, define the call names for commands

if __name__ != '__main__':
    wrbcommands.COMMANDS['hate'] = hating
    wrbcommands.COMMANDS['love'] = hating
