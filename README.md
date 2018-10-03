wolfratbot
=========
A simple, modular, multiplatform chatbot.
---------

Currently supports both Facebook, GroupMe, and IRC chatbots.

The idea behind the project is to configure a single chatbot that runs on multiple platforms,
with a simple interface for adding new platforms.  

Main loads in modules recursively from a given directory.
These modules can add commands to the bot, which are run whenever a message
contains a command, as well as add handlers to the bot which can read and handle
raw messages.  

Some of the implemented commands are:  
  - !flip     - flip a coin and send the results
  - !repeat   - repeat the rest of the message
  - !img      - send a random valid image from imgur
  - !yt       - send the first result for a YouTube search string
  - !list     - list all valid commands
  - !help     - give information on any valid command
  - !roll     - roll an n-sided die a given number of times
  - !wump     - play a game of Hunt the Wumpus

Configuration for the chatbot is stored in an encrypted config file.
The reason for the encryption is to keep GroupMe API keys secret and
Facebook passwords private.

Dependencies:
---------
  - pyyaml  
  - requests  
  - fbchat (at the moment I recommend my fork)
  - lxml  
... and a few more listed in `requirements.txt`. To install all
dependencies, run `pip install -r requirements.txt`.   

Setup:
--------
  1. Install all dependencies  
  2. Create a config file:  
     - Copy the example from the conf directory  
     - Populate for your use, saving as `conf.dtxt` under the `conf/`
		 directory (see below). If you only want to use one platform, just
		 completely omit the configurations for the other platforms.  
     - Run `make PATHTOFILE.etxt` or `make encrypt` if you want to use the default configuration path of `conf/conf.etxt`.
     - Enter encryption key  (this will create `conf.etxt` in `conf/`)  
  3. Modify main.py to have the proper paths to your modules directory
and your configuration file. Do not edit `PASSWORD`, this will be populated
automatically.  

Configuration:
---------
For facebook, you need an account for the bot. You should friend your main account,
and add the bot to a group chat.  Save the username and password for the bot in the
corresponding places of the config file.  

For groupme, [set up the bot](https://dev.groupme.com/bots), your callback URL is
your host / IP followed by your chosen port and a path for the bot. For example,
my bot is named `WolfratBot`, my host is `johnbot.me`, I listen on port `9999`, and
the path for WolfratBot is `/wrb`, so my callback URL is `http://www.johnbot.me:9999/wrb`.  
Then, in the config file, fill out the groupme port number (`9999` in my example),
the botid (from the dev.groupme website), the path (`/wrb` in my example), and
the bot name (`WolfratBot` in my example).

Running:
---------
  1. Run main.py  
  2. Enter encryption key  

TODO:
---------
  - Add support for more messaging services  
  - Work on some NLP features  
