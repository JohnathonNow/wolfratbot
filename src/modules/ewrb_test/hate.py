def hating(SENDER,MESSAGE,CMD,send):
    send.send('HATE!!!')

# Next, define the call names for commands

COMMANDS {'hate': hating,
          'love': hating}
