from datetime import timedelta


t = [int(i) for i in input().split(':')]
print(int(timedelta(hours=t[0], minutes=t[1], seconds=t[2]).total_seconds()))
