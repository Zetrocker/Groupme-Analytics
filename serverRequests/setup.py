__author__ = 'Zetrocker'

import os
import json

configFile = 'authentication.cfg'


def makeConfigFile():
    if os.path.isfile(configFile) is False:
        with open(configFile, "w+") as cfg:
            token = input('Paste O-Auth Token here: ')
            token = [token]
            json.dump(token, cfg)