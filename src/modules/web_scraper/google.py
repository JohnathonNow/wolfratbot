import requests
import re

# grab first link from google search
def g_search(SENDER, TEXT, CMD, send):
    '''Usage:   !g SEARCH
    
    Grabs the first link upon searching SEARCH.'''
    payload = {'q':TEXT.replace(CMD,'').strip()}
    r = requests.get('http://www.google.com/search',params=payload)
    regex_result = re.search('class="r"(.*a href="([^"]*)".*)h3',r.text)
    try:
        regex_groups = regex_result.groups()
        send.send("http://www.google.com"+regex_groups[1].replace("&amp;","&"))
    except:
        send.send("Search failed!")

# grab youtube video from search
def youtube(SENDER, TEXT, CMD, send):
    '''Usage:   !yt SEARCH
    
    Grabs the first youtube video upon searching SEARCH.'''
    payload = {'search_query':TEXT.replace(CMD,'').strip()}
    r = requests.get('https://www.youtube.com/results',params=payload)
    res = re.search('(watch\?v=[^"]*)',r.text).groups()
    send.send('https://www.youtube.com/'+res[0])

# Define command mappings
COMMANDS = {'!yt': youtube,
            '!g':  g_search}
HANDLERS = {}
