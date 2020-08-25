import yaml
import getpass
import os
import ircbot
import fbbot
import gmbot
import dcbot
import time
import imp
import wrbcommands
import _thread as thread

CONFIG = "../conf/conf.txt"
MODS = "modules"

PASSWORD = ""


with open(CONFIG) as in_file:
    conf = yaml.load(in_file)

for dirpath,dirs,files in os.walk(MODS):
    for filename in files:
        if '.py' in filename[-3:]:
            modname = filename[:-3]
            modpath = os.path.join(dirpath,filename)
            try:
                print("Loading {}".format(modname))
                m = imp.load_source(modname,modpath)
                wrbcommands.addModule(m)
            except Exception as E:
                print(E)
                pass
try:
    if 'facebook' in conf:
        fbot = fbbot.Fbbot(conf['facebook']['username'], conf['facebook']['password'])
        fb_thread = thread.start_new_thread(fbbot.Fbbot.listen, (fbot,))

    if 'irc' in conf:
        i = ircbot.IRCbot(conf['irc']['username'],conf['irc']['password'],
                 conf['irc']['server'], conf['irc']['channel'],
                 conf['irc']['channels'])
        irc_thread = thread.start_new_thread(i.listen, ())

    if 'groupme' in conf:
        gm_thread = thread.start_new_thread(gmbot.listen, (conf['groupme']['port'],))
        for bot in conf['groupme']['bots']:
            gmbot.addBot(bot['path'], gmbot.Gmbot(bot['botid'], bot['name']))

    if 'discord' in conf:
        for bot in conf['discord']['bots']:
            dcbot.addBot(bot)

    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Goodbye!")
# vim: sts=4 sw=4 ts=4 expandtab ft=python
