import requests,json

__name__ = 'send'

def send(message):
	url = 'https://api.groupme.com/v3/bots/post'
	bot_id = 'e18f0a0d058420de66f2e2a387' 
	text = message;
	payload = {'bot_id': bot_id, 'text': text}
	requests.post(url, data=json.dumps(payload))
