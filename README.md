wolfratbot
=========
A simple, modular chatbot.  
---------

At the moment, it is just a GroupMe bot, set up with apache and WSGI, but
soon it will be much more.   

The WSGI script is the GroupMe bot's call back.  
It loads the command handler and all python modules
in a set module directory. These modules can modify
the command handler's command dictionary to add
functionality to the bot.  

Some of the implemented commands are:  
  - !flip     - flip a coin and send the results
  - !repeat   - repeat the rest of the message
  - !img      - send a random valid image from imgur
  - !yt       - sends the first result for a YouTube search string
  - !list     - lists all valid commands
  - !help     - gives information on any valid command

TODO:
---------
  - Restructure modules such that they have their own attributes which are loaded
into the manager, rather than having them actively adding to the manager  
  - Convert to a single running server, which can then service multiple platforms, including
more than one GroupMe chat, a Facebook Messenger chat, etc.
