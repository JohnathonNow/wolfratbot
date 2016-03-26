import json, os, re, random, wrbcommands
from send import send

import ewrb_test


def application(environ, start_response):
	REQUEST_SIZE = int(environ.get('CONTENT_LENGTH',0))
	POST = 	environ['wsgi.input'].read(REQUEST_SIZE)
	JSON = json.loads(POST)

	SENDER = JSON['name']
	TEXT = JSON['text']

	wrbcommands.handle(SENDER, TEXT)
