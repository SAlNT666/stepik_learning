def parse_ranges(ranges):
    for r in ranges.split(','):
        start, end = [int(i) for i in r.split('-')]
        yield from range(start, end + 1)


print(*parse_ranges('1-2,4-4,8-10'))
