import json, os, imp, wrbcommands, logging, sys, random
from send import send

def application(environ, start_response):
    if random.randint(1, 3) != 1:
        sys.exit(0);
    BOT_NAME = 'WolfratBot'    
    MOD_DIR = '/var/www/modules'
    LOG_FILE = '/tmp/wrb.log'

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
                    m = imp.load_source(modname,modpath)
                except Exception as E:
                    logging.warning('Module %s failed to load. Exception: %s', modname, E)
                try:
                    logging.info('Adding module %s.', modname)
                    wrbcommands.addModule(m)
                except Exception as E:
                    logging.warning('Failed to read module %s. Exception: %s', modname, E)

    if SENDER != BOT_NAME:
        try:
            sender = send()
            logging.info('Recieved message from %s.', SENDER)
            wrbcommands.handle(SENDER, TEXT, sender)
        except Exception as E:
            logging.exception("CRITICAL PROBLEM! Error: %s Dump: %s", E, JSON)
