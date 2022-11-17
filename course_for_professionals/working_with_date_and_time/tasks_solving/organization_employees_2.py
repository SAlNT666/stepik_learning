from datetime import datetime


dates = [input().split()[2] for _ in range(int(input()))]
print(dates)
dates_popularity = {(d, dates.count(d)) for d in dates}
occurrence_number = max(d[1] for d in dates_popularity)
res_list = [i[0] for i in filter(lambda x: x[1] == occurrence_number, dates_popularity)]
sorted_res_list = sorted(res_list, key=lambda d: datetime.strptime(d, '%d.%m.%Y'))
print(*sorted_res_list, sep='\n')
