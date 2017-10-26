import random, re, sys

# This is the module responsible for handling executed commands

# Commands are stored in a dict mapping the command string to a command function
# Command functons take three arguments - the sender, message, and the command that was used
# (The cmd argument is passed because multiple strings can map to the same function)

# Handler functions are stored in a list, and they take the sender and message as arguments

# First, define some simple commands as functions
def repeat(SENDER, TEXT, CMD, send):
    '''Usage:   !repeat MESSAGE 

    Simply echoes the message.'''
    send.send(TEXT.replace(CMD,'',1))

def hate(SENDER, TEXT, CMD, send):
    '''Usage:   !hate PERSON 

    Tells PERSON that I hate them.'''
    send.send('Hate...')
    shortened = TEXT.replace(CMD,'',1)
    enemy = re.sub('[\W+]','',shortened.split()[0].title())
    send.send('{}, I HATE you!'.format(enemy))
    if random.randint(1,10) <= 1:
        send.send('And, {}, I hate you too!'.format(SENDER))

def flip(SENDER, TEXT, CMD, send):
    '''Usage:   !flip

    Flips a coin and sends the result to the chat.'''
    send.send(random.choice(['Heads!','Tails!']))	


def listings(SENDER, TEXT, CMD, send):
    '''Usage:   !list

    Lists all the commands you can use.'''
    commands = '\n'.join(sorted(COMMANDS))
    send.send('All of the valid commands are:')
    send.send(commands)
    send.send('''For help on a certain command, run !help CMD''')

def ihelp(SENDER, TEXT, CMD, send):
    '''Usage:   !help CMD

    Get info on !CMD.
    DO NOT TYPE THE ! BEFORE THE COMMAND!

    For a list of commands, run !list'''
    shortened = TEXT.replace(CMD,'',1)
    subarg = shortened.split()
    if subarg:
        arg = '!'+subarg[0]
        if arg in COMMANDS:
            helptext = COMMANDS[arg].__doc__
            if helptext:
                send.send(helptext)
            else:
                send.send('No help information for {}'.format(arg))
        else:
            send.send('Command {} not regonized'.format(arg))
    else:
        send.send(ihelp.__doc__)

def info(SENDER, TEXT, CMD, send):
    send.send('\n'.join(sys.path))

# Then, map the functions to command strings
COMMANDS = {
'!help': ihelp,
'!hate': hate,
'!repeat': repeat,
'!flip': flip,
'!list': listings,
'!v': info
}

# A set for storying functions that handle 
HANDLERS = {}

def addModule(m):
    try:
        COMMANDS.update(m.COMMANDS)
    except AttributeError:
        pass
    try:
        HANDLERS.update(m.HANDLERS)
    except AttributeError:
        pass

# Finally, handle the commands and call the mapped function
def handle(SENDER, TEXT, send):
    global COMMANDS
    for command in COMMANDS:
        if command.lower() in TEXT.lower():
            COMMANDS[command](SENDER,TEXT,command,send)
    for handler in HANDLERS:
        HANDLERS[handler](SENDER,TEXT,send)

