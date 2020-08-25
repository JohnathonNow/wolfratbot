import requests
import random
import re

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

# Define command mappings
COMMANDS = {
'!hate': hate,
'!roll': roll,
'!repeat': repeat,
'!flip': flip,
}
HANDLERS = {}
# vim: sts=4 sw=4 ts=4 expandtab ft=python
