"""# my_string = input()
my_string = 'ООООООРРРОРОРРРРРРР'

number_of_P = 0

for i, val in enumerate(my_string):
    if val == 'Р':
        temp_res = 0
        for val in my_string[i:]:
            if val == 'Р':
                temp_res += 1
            if val == 'О':
                i += temp_res
                break
        if temp_res > number_of_P:
            number_of_P = temp_res

print(number_of_P)"""


s = input().split('О')
print(len(max(s)))
