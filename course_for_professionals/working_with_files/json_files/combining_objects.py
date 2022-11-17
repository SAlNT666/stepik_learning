import json


with open('data1.json', encoding='utf8') as jf1, open('data2.json', encoding='utf8') as jf2:
    d1 = json.load(jf1)
    d2 = json.load(jf2)

with open('data_merge.json', 'w', encoding='utf8') as file_out:
    json.dump(d1 | d2, file_out)
