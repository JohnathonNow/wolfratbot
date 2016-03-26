from send import send
import wrbcommands


def hi(SENDER, TEXT):
	send('HI')

wrbcommands.COMMANDS['!hi'] = hi
