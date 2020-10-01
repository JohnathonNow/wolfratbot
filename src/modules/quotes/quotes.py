import yaml
import random
import os

QUOTES = os.path.dirname(__file__) + '/quotes.yaml'

def handler(SENDER, TEXT, send):
    with open(QUOTES,'r') as f:
        quotes = yaml.load(f)
    for quote in quotes:
        for trigger in quote['triggers']:
            if trigger.lower() in TEXT.lower():
                chance = 33
                if 'chance' in quote:
                    chance = quote['chance']
                if random.randint(0,100) <= chance:
                    if 'image' in quote:
                        send.sendImage(quote['image'],quote.get('quote',''))
                    else:
                        send.send(quote['quote'].format(SENDER=SENDER))
                    break

HANDLERS = {"QuoteHandler":handler}
COMMANDS = {}
# vim: sts=4 sw=4 ts=4 expandtab ft=python
