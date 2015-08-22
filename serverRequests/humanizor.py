__author__ = 'Zetrocker'
import time
import sys
import json
import os

def humanizor(groupID):
    filename = 'transcript-' + groupID + '.txt'
    #Sort JSON file
    if os.path.isfile(filename) is False:
        with open(filename, 'w+', encoding='utf-8') as f:
            f.close
    with open(filename, 'w+', encoding='utf-8') as f:
        messages = json.load(f)
        messages = sorted(messages, key=lambda k: k[u'created_at'], reverse=False)
    # sys.stdout = open(humanLogFileName, "a+")
    # theText = str
    for items in messages:
        #pull text + attachments
        # messages = sorted(messages, key=lambda k: k[u'created_at'], reverse=True)
        text = items[u'text']
        attachments = items[u'attachments']
        #append the emoji set and character if there is one
        if len(attachments) != 0:
            for attachedItems in attachments:
                if attachedItems[u'type'] == 'emoji':
                    emoji = attachedItems[u'charmap'][0]
                    text += str(emoji)
        #Print text for humans
        t = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(items[u'created_at']))
        textstring = (t, '-', items[u'name'] + ":", text)
        print(textstring)
        f.writelines(textstring)
# sys.stdout.close()
# sys.stdout = temp

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