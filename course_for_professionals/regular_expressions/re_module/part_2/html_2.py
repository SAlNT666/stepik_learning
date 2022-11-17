import re
from collections import defaultdict


tags = defaultdict(set)

for r in open(0):
    for t, a in re.findall(r'<(\w+)(.*?)>', r):
        tags[t].update(re.findall(r'([\w-]+)=', a))

for t, a in sorted(tags.items()):
    print(t + ':' + ' ' * bool(a) + ', '.join(sorted(a)))
