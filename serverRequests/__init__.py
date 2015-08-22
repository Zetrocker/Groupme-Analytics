__author__ = 'Zetrocker'
import sys
import os
import json

from serverRequests.setup import makeConfigFile

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

from serverRequests.humanizor import humanizor

makeConfigFile()

fetchgroups()

with open('groups.json', 'r+') as f:
    groups = json.load(f)
    f.close()

group = selectGroupMenu(groups)

# groupID = group[u'id']
groupID = '6135045'
fetchmessages(groupID, group)


#
# chatLogFileName = 'transcript-' + groupID + '.json'
#
# jsondata = {}
# with open(chatLogFileName, 'w+') as f:
#     jsondata = json.load(f)
#     jsondata = sorted(key=lambda k: k[u'created_at'], reverse=True)
#     f.close()
#
# humanizor(groupID)
sys.exit()

