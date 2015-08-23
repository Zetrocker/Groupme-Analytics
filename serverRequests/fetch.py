__author__ = 'Zetrocker'

import json
import requests
import time
import sys
import os
import collections

with open('configuration.cfg', 'r+') as f:
    token = json.load(f)
    token = token[u'authentication']
    f.close()


url = "https://api.groupme.com/v3/groups"

groupData = 'groups.json'

payload = {
    'Accept': 'application/json, text/javascript',
    'Accept-Charset': 'utf-8',
    'Content-Type': 'application/json',
    'Host': 'api.groupme.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.45 Safari/537.22',
    'X-Access-Token': token
}


# humanLogFileName = 'transcript-' + group + '.txt'

def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, o)


def fetchmessages(groupID, group):


    global payload
    totalmessages = group[u'messages'][u'count']
    filename = 'transcript-' + groupID + '.json'
    url = 'https://api.groupme.com/v3/groups/' + groupID + '/messages'
    jsondata = []
    limit = 100
    params = {'limit': limit}
    parsed = 0

    while parsed < totalmessages:
        r = requests.get(url, params=params, headers=payload).text
        r.encode(encoding='utf-8', errors='replace')
        r = json.loads(r, encoding='utf-8')
        messages = r[u'response'][u'messages']
        for message in messages:
            if message[u'text'] is not None:
                # for characters in message[u'text']:
                message[u'text'] = message[u'text'].encode('utf-8', errors="replace").strip()

            parsed += 1
            #this will bring back a list of the messages as a dictionary
            jsondata.append(message)
        percentcompete = parsed / totalmessages
        print('{:.1%}'.format(percentcompete), 'downloaded')
        params = {'before_id': messages[-1][u'id'], 'limit': limit}
    messagelist = []
    for dict in jsondata:
        messagelist.append(dict)
    if os.path.isfile(filename) is False:
        with open(filename, 'w+', encoding='utf8') as f:
            json.dump(messagelist, f, ensure_ascii=False, indent=2)
            f.close()
    return messagelist


def fetchgroups():
    url = "https://api.groupme.com/v3/groups"
    data = requestserverdata(url)
    metaCode = data[u'meta'][u'code']
    if metaCode != 200:
        error(metaCode)
    if os.path.isfile(groupData) is False:
        with open(groupData, "w+") as f:
            data = data[u'response']
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.close()
    else:
        groups = {}
        file = open(groupData, "w+")
        groups = (data[u'response'])
        json.dump(groups, file, ensure_ascii=False, indent=4)
        file.close()


def error(metaCode):
    print('Fetch failed with code', metaCode)
    complete = True
    return complete


def requestserverdata(url, group='', params={}):
    """

    :rtype : JSON object
    """
    global payload
    with open('configuration.cfg') as cfg:
        token = cfg.read()
        token = json.loads(token)
        token = token[u'authentication']
        cfg.close()


    r = requests.get(url, params=params, headers=payload)

    data = r.text.replace('\ufffd', ':emoji:').replace('\U0001f601', ':Grinning-Smiley-With-Smiling Eyes:')
    data = data.replace('\U0001f60d', ':Grinning-Smiley-With-Heart-Eyes').replace('\U0001f44c', ':Okay-Hand-Sign:')
    data = data.replace('\U0001f61a', ':Kissing-Face-With-Closed-Eyes:').replace('\u270b', ':Raised-Hand:')
    data = data.replace('\U0001f61c', ':Face-With-Stuck-Out-Tongue-And-Winking-Eye:')
    data = json.loads(data)
    return data


    # fetchGroups(url, params={})
    # fetchMessages(messagesURL, params={})

    # data = requestServerData(messagesURL, params={})
