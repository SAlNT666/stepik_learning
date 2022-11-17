import json


opers = {'str': lambda x: x + '!',
         'int': lambda x: x + 1,
         'float': lambda x: x + 1,
         'bool': lambda x: not x,
         'list': lambda x: x * 2,
         'dict': lambda x: x | {'newkey': None}}

with open('data.json', encoding='utf8') as jf_in,\
        open('updated_data.json', 'w', encoding='utf8') as file_out:
    updated_objects = [opers[type(i).__name__](i) for i in json.load(jf_in) if type(i).__name__ in opers]
    json.dump(updated_objects, file_out, indent=3)
