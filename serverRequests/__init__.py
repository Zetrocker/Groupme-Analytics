__author__ = 'Zetrocker'
import sys
# import os
import json

from serverRequests.setup import makeConfigFile, loadjsonreadonly

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

from serverRequests.humanizor import forHumans
makeConfigFile()

fetchgroups()

group = loadjsonreadonly(jsonfile='groups.json')
group = selectGroupMenu(group)
groupID = group[u'id']



fetchmessages(group)

chatLogFileName = 'transcript-' + groupID + '.json'
humanLogFileName = 'transcript-' + groupID + '.txt'

# with open(chatLogFileName, 'w+') as f:
#     jsondata = json.load(f)
#     # jsondata = sorted(jsondata, key=lambda k: k)
#     f.close()
#
# print(jsondata)
#
# forHumans(chatLogFileName, jsondata)
sys.exit()

