import fbchat
import wrbcommands

class Fbbot(object):
    def __init__(self, user, passw):
        self.client = fbchat.Client(user, passw)
    
    def on_chat(self, fbid, who, msg):
        if 'otherUserFbId' in fbid:
            self._chat_id = fbid['otherUserFbId']
            self._group = False
        else:
            self._chat_id = fbid['threadFbId']
            self._group = True

        if str(who) != str(self.client.uid):
            wrbcommands.handle(str(who), msg, self)

    def parseMessage(self, content):
        if 'ms' not in content: return
        for m in content['ms']:
            if m['type'] in ['delta'] and m['delta']['class'] in ['NewMessage']:
                body = m['delta']['body']
                fbid = m['delta']['messageMetadata']['threadKey']
                who  = m['delta']['messageMetadata']['actorFbId']
                self.on_chat(fbid, who, body)

    def listen(self):
        sticky, pool = self.client._getSticky()

        while True:
            try:
                self.client.ping(sticky)
                content = self.client._pullMessage(sticky, pool)
                if content:
                    self.parseMessage(content)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                pass

    def send(self, message):
        self.client.send(self._chat_id, message, self._group)

    def sendImage(self, image_url, message = ''):
        self.client.send(self._chat_id, message + image_url, self._group)        
