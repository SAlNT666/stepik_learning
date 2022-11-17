import re


word, text = input(), input()
print(len(re.findall(rf"\b{word[:-2]}[zs]e\b", text, re.I)))
