import json


with open('people.json', encoding='utf8') as jf_in:
    people = json.load(jf_in)

none_d = {k: None for i in people for k in i.keys()}

with open('updated_people.json', 'w', encoding='utf8') as jf_out:
    json.dump([none_d | i for i in people], jf_out)


# with open('people.json', encoding='utf8') as f_in:
#     people = json.load(f_in)
#
# keys = set(k for i in people for k in i)
# for d in people:
#     d.update({k: None for k in keys.difference(d)})
#
# with open('updated_people.json', 'w', encoding='utf8') as file_out:
#     json.dump(people, file_out)
