import random
import re
import sys
import wumpy
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
    try:
        enemy = re.sub('[\W+]','',shortened.split()[0].title())
        send.send('{}, I HATE you!'.format(enemy))
        if random.randint(1,10) <= 1:
            send.send('And, {}, I hate you too!'.format(SENDER))
    except:
        pass

def flip(SENDER, TEXT, CMD, send):
    '''Usage:   !flip

    Flips a coin and sends the result to the chat.'''
    send.send(random.choice(['Heads!','Tails!']))	

def roll(SENDER, TEXT, CMD, send):
    '''Usage:   !roll X,Y

    Simulates the rolling of XdY'''

    text = TEXT.split(" ")
    options = text[text.index(CMD) + 1]
    try:
        x, y = options.split(",")
        for _ in range(int(x)):
            send.send("{}".format(random.randint(1, int(y))))
    except ValueError:
        send.send("!roll requires X and Y to be integers. For help, run !help roll")

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

wumpus = wumpy.WumpController()
def wump(SENDER, TEXT, CMD, send):
    '''Usage:   !wump [n | m [cave #] | s [list of cave numbers | a]

	To start a new game, send !wump #
	To move to a different cave, send !wump m #
		eg, !wump m 10
	To shoot an arrow, send !wump s # # #
		you can shoot an arrow at a range of one to five rooms
		eg, !wump s 10
		or
		!wump s 10 12 17
	To see the number of arrows you have remaining, send !wump a

    Controls and plays the game Hunt the Wumpus'''
    shortened = TEXT.replace(CMD,'',1)
    text = shortened.split(" ")
    try:
        if len(text) == 0:
            send.send("Must give an argument for wump.  For help, run !help wump")
        if text[0] == 'n':
            send.send(wumpus.Reset())
        elif text[0] == 'm':
            try:
                send.send(wumpus.MovePlayer(int(text[1])))
            except IndexError:
                send.send("Incorrect number of arguments for m.  For help, run !help wump")
        elif text[0] == 's':
            try:
                if len(text[1:]) > 5:
                    send.send("Incorrect number of arguments for s.  For help, run !help wump")
                else:
                    send.send(wumpus.ShootArrow(int(text[1:])))
            except IndexError:
                send.send("Incorrect number of arguments for s.  For help, run !help wump")
            pass
        elif text[0] == 'a':
            send.send(wumpus.GetArrowCount)
        else:
            send.send("Not a valid argument for wump.  For help, run !help wump")
    except ValueError:
        send.send("!wump requires room numbers to be integers. For help, run !help wump")

# Then, map the functions to command strings
COMMANDS = {
'!help': ihelp,
'!hate': hate,
'!roll': roll,
'!repeat': repeat,
'!flip': flip,
'!list': listings,
'!v': info,
'!wump': wump
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

# vim: sts=4 sw=4 ts=4 expandtab ft=python
