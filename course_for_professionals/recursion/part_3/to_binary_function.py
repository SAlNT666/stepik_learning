def to_binary(number):
    return str(number % 2) if number < 2 else to_binary(number // 2) + str(number % 2)


print(to_binary(15))
