import requests
import random
import re
from HTMLParser import HTMLParser
html = HTMLParser()

def get_quote(MIN, MAX):
    BASE = 'https://www.brainyquote.com/quotes/quotes/n/'
    SUFF = '.html'
    # First choose a random quote in the range
    QUTE = random.randint(MIN, MAX)
    # Next make the request
    r_base = requests.get(BASE+str(QUTE)+SUFF)
    # Then parse it
    suf_rand = re.search('\<p class\=\"qt_{}\"\>([^<>]*)\<'.format(QUTE),r_base.text).group(1)
    return html.unescape(suf_rand)

# Grab a random Neil deGrasse Tyson quote
def bsm(SENDER, TEXT, CMD, send):
    '''Usage:   !bsm

    Grabs a random NDT quote.'''
    MIN  = 531072
    MAX  = 531166
    send.send(get_quote(MIN, MAX)+"\n\t- Black Science Man")


# Define command mappings
COMMANDS = {'!bsm': bsm}
HANDLERS = {}

