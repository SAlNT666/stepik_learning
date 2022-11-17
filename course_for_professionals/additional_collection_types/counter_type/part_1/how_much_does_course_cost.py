from collections import Counter


c = Counter(input().split(','))
max_w_len = len(max(c, key=len))
for k, v in sorted(c.items()):
    k_price = sum(map(ord, k.replace(' ', '')))
    print(f'{k.ljust(max_w_len)}: {k_price} UC x {v} = {k_price * v} UC')
