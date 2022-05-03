import json
import os


def load_coefs_dict():
    if os.path.exists('coef_dict.json'):
        with open('coef_dict.json', 'r') as read_file:
            coef_dict = json.load(read_file)
        return coef_dict
    else:
        DataWorker.dump_coefs_dict({})


def dump_coefs_dict(coef_dict):
    with open('coef_dict.json', 'w') as write_file:
        json.dump(coef_dict, write_file)

