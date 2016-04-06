import wrbcommands, send, random, os

DIR = '/home/john/wolfratbot/modules/adlib/'
ADJES = DIR + 'adjectivelist.txt'
NOUNS = DIR + 'nounlist.txt'
VERBS = DIR + 'verblist.txt'

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

def randAdje():
    return randLine(ADJES)

def randNoun():
    return randLine(NOUNS)

def randVerb():
    return randLine(VERBS)

def adlib(SENDER, TEXT, CMD):
    '''Usage:   !ad STORY

    Replaces slots in STORY with random categorical words, and sends
    the results to the chat.
    {n}     -   NOUN
    {a}     -   ADJECTIVE
    {v}     -   VERB'''
    toRep = {'{n}': randNoun, '{a}': randAdje, '{v}': randVerb}
    message = TEXT.replace(CMD,'',1);
    run = True
    while run:
        run = False
        for rep in toRep:
            new_message = message.replace(rep,toRep[rep](),1)
            if new_message != message:
                message = new_message
                run = True
    send.send(message)

wrbcommands.COMMANDS['!ad'] = adlib
