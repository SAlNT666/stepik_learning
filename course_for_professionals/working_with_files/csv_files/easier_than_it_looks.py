import csv


def condense_csv(filename, id_name):
    data = dict()
    properties = list()

    with open(filename, encoding='utf-8') as file_in:
        for row in csv.reader(file_in):
            data[row[0]] = data.get(row[0], []) + [row[-1]]
        file_in.seek(0)
        for row in csv.reader(file_in):
            if row[1] not in properties:
                properties.append(row[1])
            else:
                break

    with open('condensed.csv', 'w', newline='', encoding='utf-8') as file_out:
        writer = csv.writer(file_out)
        writer.writerow([id_name] + properties)
        for k, v in data.items():
            writer.writerow(([k] + v))

condense_csv('test_file_for_either_than_it_looks.csv', id_name='Position')
