from send import send
import random, re

__name__ = 'wrbcommands'

def repeat(SENDER, TEXT):
	send(TEXT.replace('!repeat','',1))

def hate(SENDER, TEXT):
	send('Hate...')
	shortened = TEXT.replace('!hate','',1)
	enemy = re.sub('[\W+]','',shortened.split()[0].title())
	send('{}, I HATE you!'.format(enemy))

def flip(SENDER, TEXT):
	send(random.choice(['Heads!','Tails!']))	

COMMANDS = {
'!hate': hate,
'!repeat': repeat,
'!flip': flip
}

def handle(SENDER, TEXT):
	global COMMANDS
	for command in COMMANDS:
		if command in TEXT:
			COMMANDS[command](SENDER,TEXT)
