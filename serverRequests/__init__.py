__author__ = 'Zetrocker'
import sys

from serverRequests.setup import makeConfigFile, loadgroups

from serverRequests.fetch import fetchgroups, url, messagesURL

from serverRequests.menus import selectGroupMenu

# makeConfigFile()

fetchgroups()

group = loadgroups(groupsJson='groups.json')
group = selectGroupMenu(group)


sys.exit()

