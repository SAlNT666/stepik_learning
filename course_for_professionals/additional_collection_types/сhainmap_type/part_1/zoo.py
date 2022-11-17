from collections import Counter
import json

with open('zoo.json') as jf_in:
    print(sum(Counter(i).total() for i in json.load(jf_in)))
