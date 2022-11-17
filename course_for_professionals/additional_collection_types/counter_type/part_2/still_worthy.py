from collections import Counter
import sys


results = Counter({k: int(v) for k, v in [i.split() for i in sys.stdin]})
print(results.most_common()[-2][0])
