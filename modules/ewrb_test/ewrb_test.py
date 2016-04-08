import wrbcommands, requests, send

# First define the functions that the commands call
def img(SENDER, TEXT, CMD):
    '''USAGE:   !img[COUNT]

    Grab COUNT (default 1) images from imgur.'''
    COUNT = 1
    for i in TEXT.split():
        if CMD in i:
            s = i.replace(CMD,'')
            try:
                COUNT = int(s)
            except ValueError:
                COUNT = 1
            break
    # Send COUNT images
    while COUNT > 0:
        failed = True
        while failed:
            r = requests.get('http://imgur.com/random')
            uid = r.url.split('/')[4]
            im_url = 'http://i.imgur.com/{}.png'.format(uid)
            verified = requests.get(im_url)
            failed = 'removed' in verified.url
        send.sendImage(im_url)
        COUNT -= 1


# Next, define the call names for commands

if __name__ != '__main__':
    wrbcommands.COMMANDS['!img'] = img
