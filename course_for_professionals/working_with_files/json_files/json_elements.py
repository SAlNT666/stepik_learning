import json
import sys


for k, v in json.loads(''.join(sys.stdin)).items():
    if type(v) == list:
        v = ', '.join(str(i) for i in v)
    print(f'{k}: {v}')
