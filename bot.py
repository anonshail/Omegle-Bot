from pyomegle import OmegleClient, OmegleHandler
import time

"""
    Omegle inteface for python

    /next
        starts a new conversation
    /exit
        exits chat session
"""

interests = ['discord',
             'furries',
             'friends',
             'depressed',
             'sad',
             'lgbt',
             'lgbtq',
             'emo',
             'emos',
             'depression',
             'lonely',
             'coffee',
             'tea',
             'friend',
             'reading',
             'talk',
             'converation',
             'friendship',
             'family',
             'sadness',
             'read',
             'minecraft',
             'fortnite',
             'book',
             'music',
             'technology',
             'chill',
             'song',
             'songs',
             'singing']

h = OmegleHandler(loop=True)            # session loop
c = OmegleClient(h, wpm=30, lang='en', topics=interests)  # 30 words per minute
c.start()

'''
while 1:
    input_str = raw_input('')           # string input

    if input_str.strip() == '/next':
        c.next()                        # new conversation
    elif input_str.strip() == '/exit':
        c.disconnect()                  # disconnect chat session
        break
    else:
        c.send(input_str)               # send string
'''

while True:
    input_str = "Hey! We seem to have common interests! Come to our server, and find like minded people! We'd love to see you! Invite: https://discord.gg/vzResA"
    time.sleep(5)
    c.next()
    c.send(input_str)
    c.disconnect()
    time.sleep(30) # so that we don't get banned
