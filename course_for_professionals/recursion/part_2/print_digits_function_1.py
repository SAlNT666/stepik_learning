def print_digits(n):
    print(n % 10)
    if n >= 10:
        print_digits(n // 10)


print_digits(12345)
