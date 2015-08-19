__author__ = 'Zetrocker'
import json
import requests
import time
import sys
import os


from serverRequests.setup import makeConfigFile

makeConfigFile()

from serverRequests.fetch import fetchMessages, url, params

fetchMessages(url, params, True)