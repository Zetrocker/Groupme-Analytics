__author__ = 'Zetrocker'

import sys


def selectGroupMenu(groups):
    total = len(groups)
    exitOption = total + 1
    menuItem = 0
    for x in groups:
        menuItem += 1
        print(repr(menuItem) + ')', dict(x).get(u'name'))
    print(repr(exitOption) + ')' 'Quit')
    try:
        choice = int(input("Select Group:"))
        if not (1 <= choice <= exitOption):
            raise ValueError()
    except ValueError:
        print("Invalid Option")
    else:
        selectedGroup = choice - 1
        print(groups[selectedGroup][u'name'], 'selected.')
        theGroup = groups[selectedGroup]
        return theGroup