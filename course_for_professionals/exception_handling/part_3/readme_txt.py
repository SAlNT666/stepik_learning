try:
    with open(input(), encoding='utf-8') as f_in:
        print(f_in.read())
except FileNotFoundError:
    print('Файл не найден')
