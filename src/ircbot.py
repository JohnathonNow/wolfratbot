import fbchat
import signal
import wrbcommands
import socket
import sys

class IRCbot(object):
    def __init__(self, user, passw, server, channel, channels = False):
        self.irc = IRC()
        self.user = user
        self.channels = channels
        self.passw = passw
        self.channel = None
        self.irc.connect(server, channel, user, passw)

    def on_chat(self, who, msg):
        if who != self.user:
            wrbcommands.handle(str(who), msg, self)

    def listen(self):
        while True:
            buff = self.irc.recieve()
            if len(buff) > 0 and buff[0] == ':' and 'PRIVMSG' in buff:
                 #it is a message
                 who = buff[1:].split('!')[0].strip()
                 self.channel = buff.split('PRIVMSG', 1)[1].split(':', 1)[0].strip()
                 message = buff.split('PRIVMSG', 1)[1].split(':', 1)[1].strip()
                 if not '#' in self.channel:
                     self.channel = who
                     self.on_chat(who, message)
                 elif self.channels:
                     self.on_chat(who, message)


    def send(self, message):
        for m in message.split('\n'):
            self.irc.send(self.channel, m)

    def sendImage(self, image_url, message = ''):
        self.send(message + image_url)

class IRC:
    irc = socket.socket()

    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def quit(self, channel, debug=False):
        self.irc.send("QUIT " + " :kbye...\r\n")

    def send(self, channel, msg, debug=False):
        self.irc.send("PRIVMSG " + channel + " :" + msg + "\r\n")

    def connect(self, server, channel, nick, password, debug=False):
        # TODO: error check all this
        self.irc.connect((server, 6667))
        self.irc.send("PASS " + password + "-no_mpdm_greet\r\n") 
        self.irc.send("NICK " + nick + "\r\n")
        self.irc.send("USER " + nick + " " + server + nick + " : " + nick + "\r\n") 
        self.irc.send("JOIN " + channel + "\r\n")

    def pong(self, buff, debug=False):
        if buff.find('PING') != -1:
            self.irc.send('PONG ' + buff.split()[1] + '\r\n') 

    def recieve(self, debug=False):
        buff = self.irc.recv(2040)
        self.pong(buff, debug)
        return buff
# vim: sts=4 sw=4 ts=4 expandtab ft=python
