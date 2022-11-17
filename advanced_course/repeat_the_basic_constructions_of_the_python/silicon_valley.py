# strings = [list(input()) for i in range(int(input()))]

strings = [['o', 's', 'f', 'j', 'w', 'o', 'i', 'e', 'r', 'g', 'w', 'o', 'i', 'g', 'n', 'a', 'e', 'w', 'p', 'j', 'o', 'f', 'w', 'o', 'e', 'i', 'j', 'f', 'n', 'w', 'f', 'o', 'n', 'e', 'w', 'f', 'o', 'i', 'g', 'n', 'e', 'w', 't', 'o', 'w', 'e', 'n', 'f', 'f', 'n', 'o', 'e', 'i', 'w', 'o', 'w', 'j', 'f', 'n', 'i', 'n', 'o', 'i', 'w', 'f', 'e', 'n'],
           ['a', 'n', 't', 'o', 'n'],
           ['a', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'n', 't', 'o', 'o', 'o', 'o', 'o'],
           ['e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l', 'e', 'l'],
           ['n', 't', 'o', 'n', 'e', 'e', 'e', 'e'],
           ['t', 'o', 'n', 'e', 'e'],
           ['2', '5', '3', '2', '3', '5', '2', '3', '5', 'a', '5', '3', '2', '3', '3', '5', '2', 'n', '2', '5', '2', '3', '5', '3', '5', '2', 't', '2', '5', '3', '5', '2', '3', '5', '2', '3', '2', '3', '5', 'o', 'o', '2', '3', '5', '5', '2', '3', '5', '2', '3', '5', '2', '3', 'n'],
           ['a', 'n', 't', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'n'],
           ['u', 'n', 't', 'o', 'n']]
"""
for i in strings:
    print(list(i))
"""
# РЕШЕНИЕ КИРИЛЛА ИЗ НАСТОЯЩЕГО
import re


for i, s in enumerate(input() for i in range(int(input()))):
    if re.search(r'.*a.*n.*t.*o.*n', s): print(i + 1, end=' ')


# РЕШЕНИЕ КИРИЛЛА ИЗ ПРОШЛОГО
strings = [input() for i in range(int(input()))]

for num, i in enumerate(strings):
    a_ind = i.find('a')
    n1_ind = i[a_ind:].find('n')
    if n1_ind != -1:
        t_ind = i[a_ind+n1_ind:].find('t')
        if t_ind != -1:
            o_ind = i[a_ind+n1_ind+t_ind:].find('o')
            if o_ind != -1:
                n2_ind = i[a_ind+n1_ind+t_ind+o_ind:].find('n')
                if n2_ind != -1:
                    print(num+1, end=' ')
