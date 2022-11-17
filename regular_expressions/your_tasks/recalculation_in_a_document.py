import re


text = input()


def dollars_to_rub(row):
    rounded_v = round(float(row[2].replace(',', '.')) * 59.5, 2)
    return str((rounded_v, int(rounded_v))[int(rounded_v) == rounded_v]).replace('.', ',') + ' руб'


def inches_to_cm(row):
    rounded_v = round(float(row[1].replace(',', '.')) * 2.54, 2)
    return str((rounded_v, int(rounded_v))[int(rounded_v) == rounded_v]).replace('.', ',') + ' см'


text = re.sub(r'(\$)(\d+(?:,\d+)?)', dollars_to_rub, text)
text = re.sub(r'(\d+(?:,\d+)?)( дюйм[а-я]?|")', inches_to_cm, text)

print(text)
