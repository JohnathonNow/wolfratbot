from send import send
import random, re

# This is the module responsible for handling executed commands

# First, define some simple commands as functions
def repeat(SENDER, TEXT, CMD):
    send(TEXT.replace(CMD,'',1))

def hate(SENDER, TEXT, CMD):
    '''Usage:   !hate PERSON 

    Tells PERSON that I hate them.'''
    send('Hate...')
    shortened = TEXT.replace(CMD,'',1)
    enemy = re.sub('[\W+]','',shortened.split()[0].title())
    send('{}, I HATE you!'.format(enemy))

def flip(SENDER, TEXT, CMD):
    '''Usage:   !flip

    Flips a join and sends the result to the chat.'''
    send(random.choice(['Heads!','Tails!']))	


def ihelp(SENDER, TEXT, CMD):
    '''Usage:   !help CMD

    Get info on !CMD.
    DO NOT TYPE THE ! BEFORE THE COMMAND!'''
    shortened = TEXT.replace(CMD,'',1)
    subarg = shortened.split()
    if subarg:
        arg = '!'+subarg[0]
        if arg in COMMANDS:
            helptext = COMMANDS[arg].__doc__
            if helptext:
                send(helptext)
            else:
                send('No help information for {}'.format(arg))
        else:
            send('Command {} not regonized'.format(arg))
    else:
        send(ihelp.__doc__)

# Then, map the functions to command strings
COMMANDS = {
'!help': ihelp,
'!hate': hate,
'!repeat': repeat,
'!flip': flip
}

# Finally, handle the commands and call the mapped function
def handle(SENDER, TEXT):
    global COMMANDS
    for command in COMMANDS:
        if command in TEXT:
            COMMANDS[command](SENDER,TEXT,command)


