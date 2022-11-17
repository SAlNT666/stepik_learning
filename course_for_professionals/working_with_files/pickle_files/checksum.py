import pickle


with open(input(), 'rb') as pf_in:
    obj = pickle.load(pf_in)

checksum = 0
obj_ints = list(filter(lambda x: isinstance(x, int), obj))
if obj_ints:
    if isinstance(obj, dict):
        checksum = sum(obj_ints)
    elif isinstance(obj, list):
        checksum = min(obj_ints) * max(obj_ints)

print(('Контрольные суммы не совпадают', 'Контрольные суммы совпадают')[checksum == int(input())])
