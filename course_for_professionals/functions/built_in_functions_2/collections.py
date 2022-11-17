obj = eval(input())
print(eval({list: 'obj[-1]', tuple: 'obj[0]', set: 'len(obj)'}[type(obj)]))
