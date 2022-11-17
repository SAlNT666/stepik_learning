import re


for mail in re.findall(r'(?:[01][0-9]|2[0-3]):[0-5]\d', input()):
    print(mail)
