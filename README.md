wolfratboT
=========
A simple, modular chatbot.  
---------

Current supports both Facebook and GroupMe chatbots.

Main loads in modules recursively from a given directory.
These modules can modify the command handler's command 
dictionary to add functionality to the bot.  

Some of the implemented commands are:  
  - !flip     - flip a coin and send the results
  - !repeat   - repeat the rest of the message
  - !img      - send a random valid image from imgur
  - !yt       - send the first result for a YouTube search string
  - !list     - list all valid commands
  - !help     - give information on any valid command

Configuration for the chatbot is stored in an encrypted config file.
The reason for the encryption is to keep GroupMe API keys secret and
Facebook passwords private.

Dependencies:
---------
  - pyyaml  
  - requests  
  - fbchat (at the moment I recommend thekindlyone's fork)
  - lxml  

Setup:
--------
  1. Install all dependencies  
  2. Create a config file:  
     - Copy the example from the conf directory  
     - Populate for your use, saving as a .dtxt file  
     - Run `make PATHTOFILE.etxt"  
     - Enter encryption key  
  3. Modify main.py to have the proper paths to your modules directory
and your configuration file.

Running:
---------
  1. Run main.py  
  2. Enter encryption key  

TODO:
---------
  - Finish integrating into one server program
  - Add support for more messaging services  
  - Work on some NLP features  
