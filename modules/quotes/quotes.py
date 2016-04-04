import wrbcommands, send, yaml

QUOTES = '/home/john/wolfratbot/modules/quotes/quotes.yaml'

def handler(SENDER, TEXT):
    quotes = yaml.load(file(QUOTES,'r'))
    for quote in quotes:
        for trigger in quote['triggers']:
            if trigger.lower() in TEXT.lower():
                send.send(quote['quote'].format(SENDER=SENDER))
                break

wrbcommands.HANDLERS.append(handler)
