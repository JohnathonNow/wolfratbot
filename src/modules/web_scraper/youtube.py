import requests
import re

# grab youtube video from search
def youtube(SENDER, TEXT, CMD, send):
    '''Usage:   !yt SEARCH
    
    Grabs the first youtube video upon searching SEARCH.'''
    payload = {'search_query':TEXT.replace(CMD,'').strip()}
    r = requests.get('https://www.youtube.com/results',params=payload)
    res = re.search('(watch\?v=[^"]*)',r.text).groups()
    send.send('https://www.youtube.com/'+res[0])

# Define command mappings
COMMANDS = {'!yt': youtube}
