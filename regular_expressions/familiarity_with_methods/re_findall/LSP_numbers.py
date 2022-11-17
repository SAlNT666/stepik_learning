import re


for number in re.findall(r'\d{11}', input()):
    print(number)
