import requests
import random
import re

# Grab a random SMBC comic
def smbc(SENDER, TEXT, CMD, send):
    '''Usage:   !smbc

    Grabs a random smbc comic.'''
    BASE = 'http://smbc-comics.com'
    
    # First we load the page to get the random button url
    r_base = requests.get(BASE)
    # Then parse it for the url
    suf_rand = re.search('(\?id=[0-9]*)',r_base.text).group(1)
    # Now we can get the random page
    r_rand = requests.get('{}{}'.format(BASE,suf_rand))
    # And the random image
    suf_img = re.search('(comics/[^a-z]*(png|gif|jpg|bmp))',r_rand.text).group(1)
    im_url = '{}/{}'.format(BASE,suf_img)

    send.sendImage(im_url)

# Grab a random xkcd comic
def xkcd(SENDER, TEXT, CMD, send):
    '''Usage:   !xkcd

    Grabs a random xkcd comic.'''
    BASE = 'http://c.xkcd.com/random/comic/'
    IMG_BASE = 'http://imgs.xkcd.com/'    

    # Just grab the random URL image and send it
    r = requests.get(BASE)
    suf_img = re.search('(comics/.*(png|gif|jpg|bmp))',r.text).group(1)
    im_url = '{}/{}'.format(IMG_BASE,suf_img)

    send.sendImage(im_url)


# Define command mappings
COMMANDS = {'!smbc': smbc,
            '!xkcd': xkcd}
HANDLERS = {}
