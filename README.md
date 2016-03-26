# wolfratbot
A simple, modular GroupMe bot, set up with apache and WSGI.  

The WSGI script is the bot's call back.  
It loads the command handler and all python modules
in a set module directory. These modules can modify
the command handler's command dictionary to add
functionality to the bot.  

Currently, the implemented commands are:  
  - !flip     - flip a coin and send the results
  - !repeat   - repeat the rest of the message
  - !img      - send a random valid image from imgur
