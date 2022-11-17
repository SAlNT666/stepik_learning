import re


normalize_jpeg = lambda filename: re.sub(r'jpe?g$', r'jpg', filename, flags=re.I)

print(normalize_jpeg('stepik.jPeG'))
print(normalize_jpeg('stepik.jpeg.jpg'))
