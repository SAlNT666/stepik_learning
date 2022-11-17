def is_power(number):
    if number == 1:
        return True
    elif number < 1:
        return False
    else:
        return is_power(number / 2)


print(is_power(3))
