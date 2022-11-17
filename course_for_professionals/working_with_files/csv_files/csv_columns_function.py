import csv


def csv_columns(csv_file):
    with open(csv_file, encoding="utf-8") as file:
        rows = list(csv.reader(file))
    return {key: value for key, *value in zip(*rows)}
