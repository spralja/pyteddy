import json
import shelve
from pathlib import Path
from . import commands

DB_NAME = str(Path(__file__).parent / 'templates')

def create_template(kwargs):
    name = kwargs['name']
    jsonstring = kwargs['jsonstring']
    template = json.loads(jsonstring)
    with shelve.open(DB_NAME) as db:
        db[name] = template


def get_template(kwargs):
    name = kwargs['name']
    template = {}
    with shelve.open(DB_NAME) as db:
        template = db[name]

    print(template)


def delete_template(kwargs):
    if input('Are you sure [Y/n]: ').lower() == 'y':
        name = kwargs['name']
        with shelve.open(DB_NAME) as db:
            del db[name]

        print(f'deleted {name}')


def create_from_template(kwargs):
    name = kwargs['name']
    mapping = kwargs['**mapping']
    return commands.create_package(mapping, name)