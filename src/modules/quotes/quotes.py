import yaml
import random

QUOTES = '/home/john/wolfratbot/src/modules/quotes/quotes.yaml'

def handler(SENDER, TEXT, send):
    quotes = yaml.load(file(QUOTES,'r'))
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
