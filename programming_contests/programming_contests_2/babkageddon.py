# a, b = [int(i) for i in input().split()]

a, b = -1, 1

a_sign = 1 if a >= 0 else -1
b_sign = 1 if b >= 0 else -1

if a_sign * b_sign == 1:
    print(max((abs(a), abs(b))) * 2)
else:
    x = -a
    y = b + 3 * x
    print((x + y) * 2)
