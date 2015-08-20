__author__ = 'Zetrocker'
import time
import sys
import json

def forHumans(jsonFile, humanLogFileName):
    #Sort JSON file
    data = sorted(jsonFile, key=lambda k: k[u'created_at'], reverse=False)
    sys.stdout = open(humanLogFileName, "a+")
    theText = str
    for messages in data:
        #pull text + attachments
        # messages = sorted(messages, key=lambda k: k[u'created_at'], reverse=True)
        text = messages[u'text']
        attachments = messages[u'attachments']
        #append the emoji set and character if there is one
        if len(attachments) != 0:
            for attachedItems in attachments:
                if attachedItems[u'type'] == 'emoji':
                    emoji = attachedItems[u'charmap'][0]
                    text += str(emoji)
        #Print text for humans
        t = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(messages[u'created_at']))
        print(t, '-', messages[u'name'] + ":", text)
    sys.stdout.close()
    sys.stdout = temp

# def forHumans(jsonFile, jsondata):
#
#
#     #sort JSON File
#     data = sorted(jsondata, key=lambda k: k, reverse=False)
#
#     sys.stdout = open(jsonFile, 'a+')
#     for x in data:
#         print(x)
#         for messages in x:
#             print(messages)
#             text = messages[u'text']
#             attachments = messages[u'attachments']
#             if len(attachments) != 0:
#                 for attachedItems in attachments:
#                     for charmaps in attachedItems:
#                         emoji = attachedItems[u'charmap'][charmaps]
#                         text = text + str(emoji)
#         #Print text for humans
#         t = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(messages[u'created_at']))
#         print(t, '-', messages[u'name'] + ":", text)
#     sys.stdout.close()
#     # sys.stdout = temp