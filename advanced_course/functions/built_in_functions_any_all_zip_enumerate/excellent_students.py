print(('NO', 'YES')[all([any(['5' in input() for _ in range(int(input()))]) for _ in range(int(input()))])])

# flag = False
#
# for _ in range(int(input())):
#     for i in range(int(input())):
#         mark = input().split()[1]
#         if mark == '5':
#             flag = True
#     if not flag:
#         open(0)
#         print('NO')
#         break
#     flag = False
# else:
#     print('YES')
