__author__ = 'Zetrocker'
import sys
# import os
import json

from serverRequests.setup import makeConfigFile, loadjsonreadonly

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

from serverRequests.humanizor import forHumans
makeConfigFile()

with open('configuration.cfg', 'r+') as f:
    json.load(f)
    token = {'authentication'}
    f.close()

fetchgroups()

group = loadjsonreadonly(jsonfile='groups.json')
group = selectGroupMenu(group)
groupID = group[u'id']

fetchmessages(group, token)

chatLogFileName = 'transcript-' + groupID + '.json'
humanLogFileName = 'transcript-' + groupID + '.txt'

jsondata = {}
with open(chatLogFileName, 'w+') as f:
    jsondata = json.load(f)
    jsondata = sorted(key=lambda k: k[u'created_at'], reverse=True)
    f.close()
#
# print(jsondata)
#
forHumans(chatLogFileName, jsondata)
sys.exit()

