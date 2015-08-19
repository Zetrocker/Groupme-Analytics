__author__ = 'Zetrocker'

import json
import requests
import time
import sys
import os

url = "https://api.groupme.com/v3/groups"


groupData = 'groups.json'


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

def fetchmessages(group):
    groupID = group[u'id']
    messagesURL = 'https://api.groupme.com/v3/groups/' + groupID + '/messages'
    mostRecent = group[u'messages'][u'last_message_id']
    jsonData = {'messages': []}
    chatLogFileName = 'transcript-' + group + '.json'
    fetchComplete = False
    limit = 100
    data = requestserverdata(messagesURL, params={'before_id': mostRecent, 'limit': limit})
    totalMessages = group[u'messages'][u'count']

    print(totalMessages, 'messages remain.')
    count = 0
    testLimit = 1000
    while (fetchComplete is not True):
        testLimit -= 100
        print(totalMessages - limit, 'remain')
        if data[u'meta'][u'code'] == 304 or testLimit <= 0:
            print('No more messages to fetch!')
            print('Dumping to', chatLogFileName, ".")
            if os.path.isfile(chatLogFileName) is False:
                with open(chatLogFileName, "w+") as f:
                    json.dump(jsonData, f, ensure_ascii=False, indent=4)
                    f.close()
            fetchComplete = True
            break
        if data[u'meta'][u'code'] == 200:
            messages = data[u'response'][u'messages']
            messages = zip(messages)
            first = data[u'response'][u'messages'][0][u'id']
            params = {'before_id': first, 'limit': limit}
            for x in messages:
                count += 1
                print(x[0][u'id'])
                nextMessage = {'messages': x}
                print(totalMessages)
                totalMessages -= 1
                print(totalMessages, 'remain.')
                jsonData.update(nextMessage)
            if data[u'meta'][u'code'] is not 304:
                data = requestserverdata(messagesURL, params=params)
        else:
            metaCode = data[u'meta']['code']
            print(metaCode)
            fetchComplete = True
            return fetchComplete


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
    data = r.text.replace(
        '\ufffd', ':emoji:').replace('\U0001f601', ':Grinning-Smiley-With-Smiling Eyes:').replace('\U0001f60d',
                                                                                                  ':Grinning-Smiley-With-Heart-Eyes').replace(
        '\U0001f44c', ':Okay-Hand-Sign:')
    data = json.loads(data)
    return data


    # fetchGroups(url, params={})
    # fetchMessages(messagesURL, params={})

    # data = requestServerData(messagesURL, params={})
