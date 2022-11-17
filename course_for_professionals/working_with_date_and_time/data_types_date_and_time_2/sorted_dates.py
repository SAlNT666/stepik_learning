import datetime


dates = [input() for _ in range(int(input()))]
print(*[datetime.date.fromisoformat(d).strftime('%d/%m/%Y') for d in sorted(dates)], sep='\n')
