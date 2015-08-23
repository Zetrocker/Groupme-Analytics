__author__ = 'Zetrocker'
import sys
import os
import json

from serverRequests.setup import makeConfigFile

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

from serverRequests.humanizor import humanizor

makeConfigFile()
#
fetchgroups()
#
with open('groups.json', 'r+') as f:
    groups = json.load(f)
    f.close()

group = selectGroupMenu(groups)

groupID = group[u'id']
# groupID = '6135045'
messages = fetchmessages(groupID, group)
#
# for message in messages:
#     print(message[u'id'])
#     if message [u'text'] is not None:
#
#         message[u'text'] = message[u'text'].replace('\ufffd', ':emoji:').replace('\U0001f601', ':Grinning-Smiley-With-Smiling Eyes:')\
#                     .replace('\U0001f60d', ':Grinning-Smiley-With-Heart-Eyes').replace('\U0001f44c', ':Okay-Hand-Sign:')\
#                     .replace('\U0001f61a', ':Kissing-Face-With-Closed-Eyes:').replace('\u270b', ':Raised-Hand:')\
#                     .replace('\U0001f61c', ':Face-With-Stuck-Out-Tongue-And-Winking-Eye:').replace('\u0f3c', ':Tibetan-Mark-Ang-Khang-Gyon:')\
#                     .replace('\u3064', ':Hiragana-Letter-Tu:').replace('\u25e1', ':Lower-Half-Circle:').replace('\u0f3d', ':Tibetan-Mark-Ang-Khang-Gyas:')\
#                     .replace('\U0001f62e', ':Face-With-Open-Mouth:').replace('\U0001f647', ':Person-Bowing-Deeply:').replace('\U0001f192', ':Squared-Cool:')
#         print(message[u'text'])

#
chatLogFileName = 'transcript-' + groupID + '.json'
#
# with open(chatLogFileName, encoding='utf-8') as f:
#     filestring = f.read()
#     filestring.encode(encoding='utf-8', errors='replace')
#     print(filestring)
#     # jsondata = json.load(f)
#     # jsondata = sorted(key=lambda k: k[u'created_at'], reverse=True)
#     f.close()

# humanizor(groupID, jsondata)

sys.exit()

