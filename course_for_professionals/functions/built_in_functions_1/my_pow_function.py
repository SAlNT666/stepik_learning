def my_pow(number):
    return sum(int(d) ** i for i, d in enumerate(str(number), 1))


print(my_pow(139))
