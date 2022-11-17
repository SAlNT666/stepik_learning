def add_attrs(**attrs):
    def decorator(func):
        func.__dict__.update(attrs)
        return func
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
