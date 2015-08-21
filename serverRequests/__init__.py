__author__ = 'Zetrocker'
import sys
import os
import json

from serverRequests.setup import makeConfigFile

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

from serverRequests.humanizor import forHumans

makeConfigFile()

with open('configuration.cfg', 'r+') as f:
    token = json.load(f)
    token = token[u'authentication']
    f.close()

fetchgroups()

with open('groups.json', 'r+') as f:
    groups = json.load(f)
    f.close()

group = selectGroupMenu(groups)

groupID = group[u'id']

fetchmessages(groupID, token)
#
# chatLogFileName = 'transcript-' + groupID + '.json'
# humanLogFileName = 'transcript-' + groupID + '.txt'
#
# jsondata = {}
# with open(chatLogFileName, 'w+') as f:
#     jsondata = json.load(f)
#     jsondata = sorted(key=lambda k: k[u'created_at'], reverse=True)
#     f.close()
#
# print(jsondata)
#
# forHumans(chatLogFileName, jsondata)
sys.exit()

