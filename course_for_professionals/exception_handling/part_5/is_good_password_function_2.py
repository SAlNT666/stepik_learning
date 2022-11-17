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
        raise LengthError
    elif p.islower() or p.isupper() or not any(l.isalpha() for l in p):
        raise LetterError
    elif p.isalpha():
        raise DigitError
    else:
        return True


try:
    print(is_good_password('!@#$%^&*()_+'))
except Exception as err:
    print(type(err))
