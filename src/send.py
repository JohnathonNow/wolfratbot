import requests,json

class send(object):

        def __init__(self, bot_id = 'e18f0a0d058420de66f2e2a387'):
            self.bot_id = bot_id

        # Send a test message as a GroupMe bot
        def send(self,message):
            url = 'https://api.groupme.com/v3/bots/post'
            text = message;
            payload = {'bot_id': self.bot_id, 'text': text}
            requests.post(url, data=json.dumps(payload))

        # Send an image message as a GroupMe bot
        def sendImage(self, image_url, message = ''):
            url = 'https://api.groupme.com/v3/bots/post'
            text = message;
            payload = {'bot_id': self.bot_id, 'text': text,
            'attachments': [
            {
                    'type': 'image',
                    'url': image_url
            }]}
            requests.post(url, data=json.dumps(payload))
