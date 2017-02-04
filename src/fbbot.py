import fbchat
import signal
import wrbcommands

MAX_ATTEMPTS = 3
RESTICKY_DELAY = 60*60;
class Timeout(Exception):
    def __init__(self, message, errors):
        super(Timeout, self).__init__(message)
        self.errors = errors

class Fbbot(object):
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw
        self.login();
        if self.client == None:
            print('OH NO!')
        else:
            print('Logged in!')
    
    def login(self):
        fail_count = 0
        self.client = None
        while fail_count < MAX_ATTEMPTS and self.client == None:
            try:
                self.client = fbchat.Client(self.user, self.passw)
            except:
                self.client = None
                fail_count = fail_count + 1

    def on_chat(self, fbid, who, msg):
        if 'otherUserFbId' in fbid:
            self._chat_id = fbid['otherUserFbId']
            self._group = 'user'
        else:
            self._chat_id = fbid['threadFbId']
            self._group = 'group'

        try:
            who_name = self.client.getUserInfo(who)['firstName']
        except:
            who_name = who

        if str(who) != str(self.client.uid):
            wrbcommands.handle(str(who_name), msg, self)

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
                signal.alarm(RESTICKY_DELAY);
                self.client.ping(sticky)
                content = self.client._pullMessage(sticky, pool)
                print(content)
                if content:
                    self.parseMessage(content)
            except Timeout:
                self.login()
                sticky, pool = self.client._getSticky()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                pass

    def send(self, message):
        self.client.send(self._chat_id, message, self._group)

    def sendImage(self, image_url, message = ''):
        self.client.sendRemoteImage(self._chat_id, message, self._group, image_url)
