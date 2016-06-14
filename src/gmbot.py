import requests
import json
import thread

class Gmbot(object):
    def __init__(self, bot_id = 'e18f0a0d058420de66f2e2a387'):
    self.bot_id = bot_id

    def on_chat(self, fbid, who, msg):
        wrbcommands.handle(str(who), msg, self)

    # Send a text message as a GroupMe bot
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

    def listen(self, port):
        self.socket.bind(('0.0.0.0', port))
        self.socket.listen(0) 
        while True:
            client, address = self.socket.accept()
            self.handle(client)
        thread.start_new_thread(Gmbot.handle, (self, client, ))

    def handle(self, client):
        stream = client.makefile('w+')
        data = []
        dataIn = self.stream.readline()
        while dataIn != '' and dataIn != '\r\n':
            data.append(dataIn)
            dataIn = self.stream.readline()
        print data[0]
        print data[len(data)-1]
