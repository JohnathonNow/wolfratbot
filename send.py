import os

__name__ = 'send'

def send(message):
	dir = os.path.dirname(os.path.realpath(__file__))
	os.system(dir+'/sendmessage.sh "'+message+'"')
