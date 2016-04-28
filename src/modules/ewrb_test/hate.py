def hating(SENDER,MESSAGE,CMD,send):
    send.send('HATE!!!')

# Next, define the call names for commands

wrbcommands.COMMANDS['hate'] = hating
wrbcommands.COMMANDS['love'] = hating
