import json
from operator import itemgetter
import operator
from random import randint
import re


with open('trump.json') as f:
    trump = json.load(f)

with open('keywords.json') as f:
    kwrds = json.load(f)


def returnTopics(s1):
    data = []
    for t in trump:
        if s1 in t['text'].lower():
            data.append(t['text'].lower())
    data = [re.sub('\s+', ' ', sent) for sent in data]
    data = [re.sub("\'", "", sent) for sent in data]
    # print (data)
    matchGroup = []
    verify = []
    for d in data:
        splitD = d.split(" ")
        matchedData = set(splitD) & set(kwrds)
        # print (matchedData)
        c = dict.fromkeys(matchedData, 0)
        matchedList = list(set(splitD) & set(kwrds))
        for m in matchedData:
            if m in verify:
                index1 = verify.index(m)
                matchGroup[index1]['count'] += 1
                for li in matchedList:
                    if li in matchGroup[index1]['matches']:
                        matchGroup[index1]['matches'][li] += 1

            elif m not in verify:
                hashArr = {
                    'word': m,
                    'count': 1,
                    'matches': c
                }
                matchGroup.append(hashArr)
                verify.append(m)
    newlist = sorted(matchGroup, key=lambda k: k['count'])
    newlist.reverse()
    slicedList = newlist[:81]
    dataArr = []
    for index, sort in enumerate(slicedList):
        if index <= 80:
            sorted_x = sorted(sort['matches'].items(), key=operator.itemgetter(1))
            sorted_x.reverse()
            wordArr = []
            xSlice = sorted_x[:10]
            for xS in xSlice:
                wordArr.append(xS[0])
            hash2 = {
                'word': sort['word'],
                'data': index/2,
                'matches': wordArr
            }
            dataArr.append(hash2)
    print (dataArr)
    return dataArr, s1
