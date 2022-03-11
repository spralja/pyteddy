from .. import _db

import shelve
import string
import sys

from pathlib import Path

__module__ = sys.modules[__name__]

COMMAND = Path(__file__).name.split('.')[0]


def execute(**kwargs):
    subcommand = kwargs.pop('subcommand')
    getattr(__module__, subcommand)(**kwargs)


def load(name, path):
    path = Path(path)
    template = {path.name: template_from_path(path)}
    ckwargs = {name: template}
    _db.update('template', ckwargs)
    print(_db.get('template')[name])


def template_from_path(path: Path):
    """
    Recursively converts a path to a dictionary by reading all the files
    example:

    test/
        LICENSE ('license text')
        .gitignore ('#gitignore body')

    converts to:
        
    {
        'test': {
            'LICENSE': 'license text',
            '.gitignore': '#gitignore body',
        }
    }
    """

    if path.is_dir():
        dct = {}
        for sub_path in path.iterdir():
            dct[sub_path.name] = template_from_path(sub_path)

        return dct
    
    with open(path, 'r') as file:
        return file.read()



def create(name, path, context):
    path = Path(path)
    splitted_context = split_context(context)
    true_context = _db.get('config')

    true_context.update(splitted_context)

    template = _db.get('template')[name]

    relieved_template = relieve_template(template, true_context)

    create_path_from_template(path, relieved_template)


def create_path_from_template(path, template):
    for name, content in template.items():
        sub_path = path / name
        if type(content) is dict:
            sub_path.mkdir()
            return create_path_from_template(sub_path, content)
        
        with open(sub_path, 'w') as file:
            file.write(content)
        


def split_context(context):
    if context is None:
        return {}

    splitted_context = {}
    for unit in context:
        key, value = unit.split('=')
        splitted_context[key] = value
    
    return splitted_context


def relieve_template(template, context):
    if type(template) is dict:
        return {relieve_template(name, context): relieve_template(content, context) for name, content in template.items()}

    return string.Template(template).substitute(context)


def delete(name):
    _db.delete('template', name)
    