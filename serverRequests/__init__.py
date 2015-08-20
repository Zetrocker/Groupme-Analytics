__author__ = 'Zetrocker'
import sys

from serverRequests.setup import makeConfigFile, loadgroups

from serverRequests.fetch import fetchgroups,fetchmessages

from serverRequests.menus import selectGroupMenu

# makeConfigFile()

fetchgroups()

group = loadgroups(groupsJson='groups.json')
group = selectGroupMenu(group)

fetchmessages(group)

sys.exit()

