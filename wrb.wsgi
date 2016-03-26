import json, os, imp, wrbcommands
from send import send

def application(environ, start_response):
    REQUEST_SIZE = int(environ.get('CONTENT_LENGTH',0))
    POST = 	environ['wsgi.input'].read(REQUEST_SIZE)
    JSON = json.loads(POST)
    
    SENDER = JSON['name']
    TEXT = JSON['text']
    
    
    MOD_DIR = '/var/www/modules'
    
    for dirpath,dirs,files in os.walk(MOD_DIR):
        for filename in files:
            if '.py' in filename[-3:]:
                modname = filename[:-3]
                modpath = os.path.join(dirpath,filename)
                imp.load_source(modname,modpath)

    wrbcommands.handle(SENDER, TEXT)
