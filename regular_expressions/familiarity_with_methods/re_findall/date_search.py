import re


for date in re.findall(r'(?:\d\d[.\/]\d\d[.\/]\d\d\d\d)|(?:\d\d\d\d[.\/]\d\d[.\/]\d\d)', input()):
    print(date)
