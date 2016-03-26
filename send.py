import requests,json

__name__ = 'send'

def send(message, bot_id = 'e18f0a0d058420de66f2e2a387'):
	url = 'https://api.groupme.com/v3/bots/post'
	text = message;
	payload = {'bot_id': bot_id, 'text': text}
	requests.post(url, data=json.dumps(payload))

def sendImage(image_url, message = '', bot_id = 'e18f0a0d058420de66f2e2a387'):
	url = 'https://api.groupme.com/v3/bots/post'
	text = message;
	payload = {'bot_id': bot_id, 'text': text,
	'attachments': [
	{
      		'type': 'image',
      		'url': image_url
	}
	]
	}
	requests.post(url, data=json.dumps(payload))
