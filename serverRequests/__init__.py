__author__ = 'Zetrocker'
import sys

from serverRequests.setup import makeConfigFile, loadgroups

from serverRequests.fetch import fetchGroups, url, messagesURL

from serverRequests.menus import selectGroupMenu

# makeConfigFile()

# fetchGroups(url)


group = loadgroups(groupsJson='groups.json')

group = selectGroupMenu(group)

groupID = group[u'id']

print(group)

sys.exit()

