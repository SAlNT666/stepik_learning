from collections import Counter


def print_bar_chart(data, mark):
    data_dict = Counter(data)
    max_len = len(max(data_dict, key=len))
    print(*[f'{k.ljust(max_len)} |{mark * v}' for k, v in data_dict.most_common()], sep='\n')


languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')
