def convert(number):
    return f'{number:b}', f'{number:o}', f'{number:X}'


print(convert(15))
print(convert(-24))
