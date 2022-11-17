def is_good_password(p):
    return all((len(p) > 8, any(i.islower() for i in p), any(i.isupper() for i in p), any(i.isdigit() for i in p)))


print(is_good_password('мойпарольсамыйлучший'))
