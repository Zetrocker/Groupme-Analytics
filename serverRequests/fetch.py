__author__ = 'Zetrocker'

import json
import requests
import time
import sys
import os

token = str

with open('authentication.cfg') as cfg:
    token = cfg.read()
    token = json.loads(token)
    token = token[0]
    cfg.close()

group = '1324623'

url = "https://api.groupme.com/v3/groups"
messagesURL = url + "/" + group + '/messages'

payload = {
    'Accept': 'application/json, text/javascript',
    'Accept-Charset': 'utf-8',
    'Content-Type': 'application/json',
    'Host': 'api.groupme.com',
    'Referer': 'https://api.groupme.com/v3/groups/' + group,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.45 Safari/537.22',
    'X-Access-Token': token
}

groupData = 'groups.json'
chatLogFileName = 'transcript-' + group + '.json'
humanLogFileName = 'transcript-' + group + '.txt'
params = {}

mostRecent = int

def default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, o)


# print('data has now been put to json.loads(). This makes the type: ', type(data))
# count = data[u'response'][u'count']
# print(data)
# data = data[u'response'][u'messages']
# data[u'response'][u'messages']
# data = default(data, data)
# print(iter(data))
# print(data)

def fetchMessages(messagesURL, params):
    mostRecent = mostRecentIs(group)
    jsonData = {'messages': []}
    fetchComplete = False
    limit = 100
    data = requestServerData(messagesURL, params={'before_id': mostRecent, 'limit': limit})
    totalMessages = int
    file = open(groupData, 'r+')
    with file as f:
        index = json.load(f)
        # totalMessages = groupdata[0][u'id'][group][0]
        i = -1
        for x in f:
            i += 1
            id = index[i][u'id']
            if id == group:
                totalMessages = index[i][u'messages'][u'count']
        f.close()

    print(totalMessages, 'messages remain.')
    count = 0
    testLimit = 1000
    while (fetchComplete is not True):
        testLimit -= 1
        print(totalMessages, 'remain')
        if data[u'meta'][u'code'] == 304 or testLimit <= 0:
            print('No more messages to fetch!')
            print('Dumping to', chatLogFileName, ".")
            if os.path.isfile(chatLogFileName) is False:
                with open(chatLogFileName, "w+") as f:
                    json.dump(jsonData, f, ensure_ascii=False, indent=4)
                    f.close()
            fetchComplete = True
            return fetchComplete
        if data[u'meta'][u'code'] == 200:
            messages = data[u'response'][u'messages']
            messages = zip(messages)
            first = data[u'response'][u'messages'][0][u'id']
            params= {'before_id': first, 'limit': limit}
            for x in messages:
                count += 1
                print(x[0][u'id'])
                nextMessage = {'messages': x}
                print(totalMessages)
                totalMessages -= 1
                print(totalMessages, 'remain.')
                jsonData.update(nextMessage)
            if data[u'meta'][u'code'] is not 304:
                data = requestServerData(messagesURL, params=params)
        else:
            metaCode = data[u'meta']['code']
            print(metaCode)
            fetchComplete = True
            return fetchComplete

def fetchGroups(url, params):
        data = requestServerData(url, params)
        metaCode = data[u'meta'][u'code']
        if metaCode != 200:
            error(metaCode)
        if os.path.isfile(groupData) is False:
            with open(groupData, "w+") as f:
                data = data[u'response']
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.close()
        else:
            file = open(groupData, "w+")
            data = data[u'response']
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.close()

def error(metaCode):
            print('Fetch failed with code', metaCode)
            complete = True
            return complete


def mostRecentIs(group) -> object:
    """

    :rtype : int of the most recent ID of the group selected
    """
    global groupData
    with open(groupData) as f:
        data = f.read()
    data = json.loads(data)
    f.close()
    for x in data:
        if x[u'id'] == group:
            mostRecentMessageID = x[u'messages'][u'last_message_id']
            return mostRecentMessageID

def requestServerData(url, params):
    """

    :rtype : JSON object
    """
    global payload
    r = requests.get(url, params=params, headers=payload)
    data = r.text.replace(
        '\ufffd', ':emoji:').replace('\U0001f601', ':Grinning-Smiley-With-Smiling Eyes:').replace('\U0001f60d', ':Grinning-Smiley-With-Heart-Eyes').replace('\U0001f44c', ':Okay-Hand-Sign:')
    data = json.loads(data)
    return data


fetchGroups(url, params={})
fetchMessages(messagesURL, params={})

# data = requestServerData(messagesURL, params={})