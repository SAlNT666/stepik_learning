import datetime


counter = 0
while True:
    d = input()
    if d == 'end':
        break
    d_nums = d.split('.')
    try:
        datetime.date(int(d_nums[2]), int(d_nums[1]), int(d_nums[0]))
        counter += 1
        print('Корректная')
    except ValueError:
        print('Некорректная')

print(counter)
