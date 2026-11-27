import json


def read_data(filename: str) -> list:
    open_file = open(f'data/{filename}', 'r')
    data = json.loads(open_file.read())
    open_file.close()

    return data
