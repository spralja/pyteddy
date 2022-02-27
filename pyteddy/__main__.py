import argparse
from string import Template
from os.path import join, relpath
from os import getcwd, mkdir
from venv import EnvBuilder
import shutil
from pathlib import Path

class File:
    def __init__(self, path, template_path):
        self.path = path
        self.template_path = template_path
        template_file = open(template_path, 'r')
        self.template = template_file.read()
        template_file.close()

template_dirs = ('$package_name', 'tests')
location = relpath(join(Path(__file__).parent.absolute(), 'templates'))
files = (
    join('$package_name', '__init__.py'), 
    join('tests', '__init__.py'),
    '.gitignore',
    'LICENSE',
    'pyproject.toml',
    'README.md',
    'requirements.txt',
    'setup.cfg',
    )
template_files = (join(location, file) for file in files)


def copy_folder(*, package_name, user_name, user_email, organisation, repository_name):
    template_dict = locals()
    def templateify(_str):
        nonlocal template_dict
        template = Template(_str)
        return template.substitute(template_dict)

    for template_dir in template_dirs:
        mkdir(templateify(join('$package_name', '$package_name', template_dir)))

    temp = {}
    for template_file, name in zip(template_files, files):
        file = open(template_file, 'r')
        temp[templateify(name)] = templateify(file.read())
        file.close()

    for name, content in temp.items():
        file = open(templateify(join('$package_name', '$package_name', name)), 'w')
        file.write(content)
        file.close()


if __name__ == '__main__':
    print(location)
    parser = argparse.ArgumentParser(description='pyhon project manager')
    parser.add_argument('--package-name', help='package name', required=True)
    parser.add_argument('--user-name', help='User\'s name', required=True)
    parser.add_argument('--user-email', help='User\'s email', required=True)
    parser.add_argument('--organisation', help='Github repostiory\'s organisation', required=True)
    parser.add_argument('--repository-name', help='Github repostory name', required=True)

    args = parser.parse_args()
    package_name = args.package_name
    print(args.__dict__)
    mkdir(package_name)
    env_builder = EnvBuilder()
    env_builder.create(package_name)
    package_dir = join(package_name, package_name)
    mkdir(package_dir)
    copy_folder(**args.__dict__)
    
