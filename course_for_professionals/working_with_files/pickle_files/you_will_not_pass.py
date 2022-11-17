import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as pf_out:
        pickle.dump(list(filter(lambda x: type(x) == typename, objects)), pf_out)
