from string import ascii_letters, ascii_lowercase, ascii_uppercase


def verification(login, password, success, failure):
    if not any(i in ascii_letters for i in password):
        failure(login, 'в пароле нет ни одной буквы')
    elif not any(i in ascii_uppercase for i in password):
        failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not any(i in ascii_lowercase for i in password):
        failure(login, 'в пароле нет ни одной строчной буквы')
    elif not any(i.isdigit() for i in password):
        failure(login, 'в пароле нет ни одной цифры')
    else:
        success(login)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
