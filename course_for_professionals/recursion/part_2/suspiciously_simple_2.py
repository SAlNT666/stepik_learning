def count_up_to_100(n=1):
    print(n)
    if n < 100:
        count_up_to_100(n + 1)


count_up_to_100()
