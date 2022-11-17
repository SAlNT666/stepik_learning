import json


try:
    with open(input(), encoding='utf-8') as jf_in:
        print(json.load(jf_in))
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')
