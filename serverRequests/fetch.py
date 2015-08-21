__author__ = 'Zetrocker'

import json
import requests
import time
import sys
import os

url = "https://api.groupme.com/v3/groups"

groupData = 'groups.json'


# humanLogFileName = 'transcript-' + group + '.txt'

def makepayload(groupID, token):
    payload = {
        'Accept': 'application/json, text/javascript',
        'Accept-Charset': 'utf-8',
        'Content-Type': 'application/json',
        'Host': 'api.groupme.com',
        'Referer': 'https://api.groupme.com/v3/groups/' + groupID,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.45 Safari/537.22',
        'X-Access-Token': token
    }
    return payload


def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, o)


def fetchmessages(groupID, token):
    payload = {
        'Accept': 'application/json, text/javascript',
        'Accept-Charset': 'utf-8',
        'Content-Type': 'application/json',
        'Host': 'api.groupme.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.45 Safari/537.22',
        'X-Access-Token': token
    }
    url = str('https://api.groupme.com/v3/groups/' + repr(groupID) + '/messages')
    data = requests.get(url, params={}, headers=payload).json()
    jsondata = []
    complete = False
    count = 0
    while complete is not True:

        data = data[u'response'][u'messages']
        for messages in data:

            if messages[u'text'] is not None:
                for text in messages[u'text']:
                    text = text.encode('utf-8').strip()
            else:
                text = ':something was weird here:'

            count += 1
            jsondata.append(messages)
            # print(messages)
        print(count)
        if len(data) < 20:
            with open('test.json', 'a+') as test:
                json.dump(jsondata, test, indent=4, ensure_ascii=False, check_circular=False)
                test.close()
            complete = True
        else:
            params = {'before_id': data[-1][u'id']}
            data = requests.get(messagesURL, params=params).json()
        return jsondata


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
    with open('configuration.cfg') as cfg:
        token = cfg.read()
        token = json.loads(token)
        token = token[u'authentication'][0]
        cfg.close()

    payload = {
        'Accept': 'application/json, text/javascript',
        'Accept-Charset': 'utf-8',
        'Content-Type': 'application/json',
        'Host': 'api.groupme.com',
        'Referer': 'https://api.groupme.com/v3/groups/' + group,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.45 Safari/537.22',
        'X-Access-Token': token
    }

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
