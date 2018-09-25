import json
import re

with open('trump.json', encoding='utf-8') as f:
    trump = json.load(f)
    
with open('keywords.json', encoding='utf-8') as f:
    keywords = json.load(f)
        
# source
# text
# created_at
# retweet_count
# favorite_count
# is_retweet
# id_str
data = []
for t in trump:
    data.append(t['text'].lower())
    
for d in data:
    splitD = d.split(" ")
    dataIntersection = set(splitD) & set(keywords)
    print (dataIntersection)