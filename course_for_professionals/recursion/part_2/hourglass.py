def hourglass(n=4):
    def print_hourglass(i):
        if i > 1:
            print(' ' * int(n / 2) * (n - i) + str(n - i + 1) * i * n)
            print_hourglass(i - 1)
        print(' ' * int(n / 2) * (n - i) + str(n - i + 1) * i * n)
    print_hourglass(n)


hourglass()
