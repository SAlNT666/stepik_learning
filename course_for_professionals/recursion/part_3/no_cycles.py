def no_cycles(number):
    if number > 0:
        print(number)
        no_cycles(number - 5)
    print(number)


no_cycles(int(input()))
