# медленнее
#
# import re
#
#
# def convert(string):
#     s = re.findall(r'[a-zа-яё]', string)
#     l = re.findall(r'[A-ZА-ЯЁ]', string)
#     return string.upper() if len(l) > len(s) else string.lower()


def convert(string):
    if sum(1 if s.isupper() else -1 for s in string if s.isalpha()) > 0:
        return string.upper()
    return string.lower()


print(convert('BEEgeekb4k1ge kuGKYF IYJFKDFUYR8687TGTD65DFHvhgdhjgcvj,hv,jrk6uerkuyfvjvjmDUTDUKYFVKNV,JFMVJYRYFV N  KUTIUL THKUT'))
