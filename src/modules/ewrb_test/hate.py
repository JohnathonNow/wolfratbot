def hating(SENDER,MESSAGE,CMD,send):
    send.send('HATE!!!')

# Next, define the call names for commands

COMMANDS = {'hate': hating,
            'love': hating}
HANDLERS = {}
# vim: sts=4 sw=4 ts=4 expandtab ft=python
