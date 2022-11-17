import datetime


all_data = []

with open('diary.txt', encoding='utf-8') as diary:
    for row in diary:
        date = datetime.datetime.strptime(row, '%d.%m.%Y; %H:%M\n')
        new_data = diary.readline()
        data = ''
        while new_data.rstrip():
            data += new_data
            new_data = diary.readline()

        all_data.append((date, data.rstrip()))

for row in sorted(all_data, key=lambda x: x[0]):
    print(row[0].strftime('%d.%m.%Y; %H:%M'), row[1], sep='\n', end='\n\n')
