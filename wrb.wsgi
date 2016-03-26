import json, os, re
from send import send

def application(environ, start_response):
	REQUEST_SIZE = int(environ.get('CONTENT_LENGTH',0))
	POST = 	environ['wsgi.input'].read(REQUEST_SIZE)
	JSON = json.loads(POST)

	SENDER = JSON['name']
	TEXT = JSON['text']

	if '!repeat' in TEXT:
		send(TEXT.replace('!repeat','',1))

	if '!hate' in TEXT:
		shortened = TEXT.replace('!hate','',1)
		enemy = re.sub('[\W+]','',shortened.split()[0].title())
		send(enemy+', I HATE you!')
