from sys import stdin
from datetime import date


dates = [date.fromisoformat(dt.strip()) for dt in stdin]
print((max(dates) - min(dates)).days)
