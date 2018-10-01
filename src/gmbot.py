import requests
import json
import thread
import socket
import wrbcommands

MAX_ATTEMPTS = 300

# Dict containing the Gmbots and their url paths
BOTS = {}

class Gmbot(object):
    def __init__(self, bot_id='e0b290e710754bc97a547b8ab5', bot_name='Test'):
        self.bot_id = bot_id
        self.bot_name = bot_name

    def on_chat(self, who, msg):
        if who != self.bot_name:
            wrbcommands.handle(who, msg, self)

    # Send a text message as a GroupMe bot
    def send(self,message):
        url = 'https://api.groupme.com/v3/bots/post'
        text = message;
        payload = {'bot_id': self.bot_id, 'text': text}
        requests.post(url, data=json.dumps(payload))

    # Send an image message as a GroupMe bot
    def sendImage(self, image_url, message=''):
        url = 'https://api.groupme.com/v3/bots/post'
        text = message;
        payload = {'bot_id': self.bot_id, 'text': text,
        'attachments': [
        {
                'type': 'image',
                'url': image_url
        }]}
        requests.post(url, data=json.dumps(payload))

def addBot(path='/test', bot=Gmbot()):
    BOTS[path] = bot
        
def listen(port=9999):
    sock = None
    failures = 0
    while sock == None and failures < MAX_ATTEMPTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
        except:
            sock = None
            failures = failures + 1
    if sock != None:
        print("GMbot Connected!")
        try:
            sock.listen(0) 
            while True:
                client, address = sock.accept()
                thread.start_new_thread(handle, (client, ))
        except KeyboardInterrupt:
            sock.close()
            raise
    else:
        print("GMbot could not listen!")

def handle(client):
    stream = client.makefile('w+')

    data = []
    dataIn = stream.readline()
    while dataIn != '' and dataIn != '\r\n':
        data.append(dataIn)
        dataIn = stream.readline()

    bot = data[0].split()[1]
    #print bot
    stream.write('\r\n')
    stream.flush()

    while dataIn != '':
        data.append(dataIn)
        dataIn = stream.readline()

    msgdata = json.loads(data[len(data)-1])
    msgtxt = msgdata['text']
    msgsender = msgdata['name']

    #print msgtxt
    #print msgsender
    
    stream.close()
    
    if bot in BOTS:
        BOTS[bot].on_chat(msgsender, msgtxt)
        
# Test script
if __name__ == '__main__':
    addBot()
    listen()
# vim: sts=4 sw=4 ts=4 expandtab ft=python
