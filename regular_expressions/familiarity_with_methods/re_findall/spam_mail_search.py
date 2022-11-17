import re


for mail in re.findall(r'[0-9A-Za-z_-]+@[0-9A-Za-z_-]+\.(?:com|ru)', input()):
    print(mail)
