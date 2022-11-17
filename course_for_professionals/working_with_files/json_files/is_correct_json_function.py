import json


def is_correct_json(string):
    try:
        json.loads(string)
    except json.decoder.JSONDecodeError:
        return False
    else:
        return True


print(is_correct_json('number = 17'))
