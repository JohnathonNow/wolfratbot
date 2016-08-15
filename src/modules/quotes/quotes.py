import yaml
import random

QUOTES = '/home/john/wolfratbot/src/modules/quotes/quotes.yaml'

def handler(SENDER, TEXT, send):
    if random.randint(1,3) == 1:
        quotes = yaml.load(file(QUOTES,'r'))
        for quote in quotes:
            for trigger in quote['triggers']:
                if trigger.lower() in TEXT.lower():
                    if 'image' in quote:
                        send.sendImage(quote['image'],quote.get('quote',''))
                    else:
                        send.send(quote['quote'].format(SENDER=SENDER))
                    break

HANDLERS = {"QuoteHandler":handler}
COMMANDS = {}
