from datetime import datetime


employees = [input().split() for _ in range(int(input()))]
oldest_employee = min(employees, key=lambda x: datetime.strptime(x[2], '%d.%m.%Y'))

print(oldest_employee[2], end=' ')
numb_of_oldest_dates = [d[2] for d in employees].count(oldest_employee[2])
print(numb_of_oldest_dates if numb_of_oldest_dates > 1 else f'{oldest_employee[0]} {oldest_employee[1]}')
