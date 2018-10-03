import wrbcommands
import discord
import asyncio

loop = asyncio.get_event_loop()

BOTS = {}

class Dcbot(discord.Client):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.channel = None

    async def on_message(self, message):
        print(message.content)
        print(message.author)
        print(message.channel)
        print(self.user)
        if message.author != self.user:
            self.channel = message.channel
            wrbcommands.handle(message.author, message.content, self)

    def send(self, message):
        print(message)
        loop.create_task(self.send_message(self.channel, message))

    def sendImage(self, image_url, message=''):
        self.send(message + image_url)

    def begin(self):
        self.run(self.token)

def addBot(token):
    BOTS[token] = Dcbot(token)
    BOTS[token].begin()
        
if __name__ == '__main__':
    TOKEN = 'NDk2ODc0NzcwMjM1OTE2MzE5.DpW-iw.qN6rd4G2NBsR-BMzLhivrYwR7S8'
    addBot(TOKEN)
        
# vim: sts=4 sw=4 ts=4 expandtab ft=python
