__author__ = 'Zetrocker'

import os
import json

configFile = 'configuration.cfg'


def makeConfigFile():
    if os.path.isfile(configFile) is False:
        open(configFile, 'w+')
        with open(configFile, "w+") as cfg:
            token = input('Paste O-Auth Token here: ')
            token = {'authentication': [token]}
            json.dump(token, cfg)
            cfg.close()