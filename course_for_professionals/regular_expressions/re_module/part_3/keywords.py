import re
from keyword import kwlist


print(re.sub(rf"\b({'|'.join(kwlist)})\b", '<kw>', input(), flags=re.I))
