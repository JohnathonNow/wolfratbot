import random
import os
import re

DIR = '/home/john/wolfratbot/src/modules/adlib/'
ADJES = DIR + 'adjectivelist.txt'
NOUNS = DIR + 'nounlist.txt'
VERBS = DIR + 'verblist.txt'

def sentenceCase(text):
    return re.sub("(^|[.!?]\s*)(\S)",
                  lambda m: m.group(1) + m.group(2).upper(),
                  text)

def randLine(fname):
    fsize = os.path.getsize(fname)
    off = random.randrange(fsize)
    f = open(fname)
    f.seek(off) 
    f.readline()  
    line = f.readline()
    if len(line) == 0:
        f.seek(0)
        line = f.readline()
    f.close()   
    return line.strip()

def adlib(SENDER, TEXT, CMD, send):
    '''Usage:   !ad STORY

    Replaces slots in STORY with random categorical words, and sends
    the results to the chat.
    {n}     -   NOUN
    {a}     -   ADJECTIVE
    {v}     -   VERB'''
    toRep = {'{n}': NOUNS, '{a}': ADJES, '{v}': VERBS}
    message = TEXT.replace(CMD,'',1);
    if message == '':
        send.send('You don\'t seem to know what you\'re doing.\nTry !help ad');
    else:
        for rep in toRep:
            while rep in message:
                message = message.replace(rep,randLine(toRep[rep]),1)

        send.send(sentenceCase(message.strip()))

COMMANDS = {'!ad': adlib}
HANDLERS = {}
