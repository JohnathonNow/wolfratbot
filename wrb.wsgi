import json, os, imp, wrbcommands, logging
def application(environ, start_response):
    
    MOD_DIR = '/var/www/modules'
    LOG_FILE = '/tmp/loader.log'
    
    logging.basicConfig(filename=LOG_FILE,level=logging.WARNING)
    
    REQUEST_SIZE = int(environ.get('CONTENT_LENGTH',0))
    POST = 	environ['wsgi.input'].read(REQUEST_SIZE)
    JSON = json.loads(POST)
    
    SENDER = JSON['name']
    TEXT = JSON['text']
        

    for dirpath,dirs,files in os.walk(MOD_DIR):
        for filename in files:
            if '.py' in filename[-3:]:
                modname = filename[:-3]
                modpath = os.path.join(dirpath,filename)
                try:
                    imp.load_source(modname,modpath)
                except:
                    logging.warning('Module {} failed to load.'.format(modname))


    wrbcommands.handle(SENDER, TEXT)
