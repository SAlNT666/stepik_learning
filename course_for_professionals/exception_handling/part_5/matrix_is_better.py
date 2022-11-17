class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(p):
    if len(p) < 9:
        raise LengthError('LengthError')
    elif p.islower() or p.isupper() or not any(l.isalpha() for l in p):
        raise LetterError('LetterError')
    elif p.isalpha():
        raise DigitError('DigitError')
    else:
        return True


invalid_p = True

while invalid_p:
    try:
        is_good_password(input())
    except Exception as err:
        print(err)
    else:
        invalid_p = False
        print('Success!')
