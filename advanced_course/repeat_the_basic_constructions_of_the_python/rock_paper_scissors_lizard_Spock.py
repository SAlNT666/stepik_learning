# put your python code here
# first, second = input(), input()
first = 'камень'
second = 'Спок'

var = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок',
       'ножницы', 'бумага', 'камень', 'ящерица', 'Спок']

print(var[5:])

first_ind = var[4:].index(first) + 4
print(var[first_ind-5:first_ind])
second_ind = var[first_ind-4:first_ind+1].index(second)
print(first_ind)
print(second_ind)


var = var[first_ind-4:first_ind+1]
print(var)

first_ind = 4
if first_ind - second_ind == 2 or first_ind - second_ind == 4:
    print('Тимур')
elif second_ind == first_ind:
    print('ничья')
else:
    print('Руслан')
