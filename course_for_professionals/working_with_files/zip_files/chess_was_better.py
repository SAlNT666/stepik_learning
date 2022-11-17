from zipfile import ZipFile
import json


arsenal_members = list()
with ZipFile('data.zip') as zf_in:
    for f in filter(lambda x: x.filename[-5:] == '.json',zf_in.infolist()):
        with zf_in.open(f) as jf_in:
            try:
                footballer = json.loads(jf_in.read().decode())
            except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                pass
            else:
                if footballer['team'] == 'Arsenal':
                    arsenal_members.append(footballer['first_name'] + ' ' + footballer['last_name'])

print(*sorted(arsenal_members), sep='\n')
