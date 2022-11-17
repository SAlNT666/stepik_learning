import pickle
import sys


with open(input(), 'rb') as pf_in:
    func = pickle.load(pf_in)

print(func(*[i.rstrip() for i in sys.stdin]))
