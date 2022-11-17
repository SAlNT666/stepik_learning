import re


print(bool(re.search(r'^(?:\+?7|8) ?\(?\d{3}\)? ?(?:\d[ \-]?){7}\b', input())))
