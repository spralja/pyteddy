from . import get_template
from .templates import releif_template

import argparse
from string import Template
from os import mkdir
from venv import EnvBuilder
from pathlib import Path
from pprint import PrettyPrinter
import sys
import traceback

pprint = PrettyPrinter


def create_directory(releived_template, path, mapping):
    path.mkdir()

    for name, content in releived_template.items():
        if type(content) is dict:
            create_directory(content, path / name, mapping)
        else:
            create_file(content, path / name)


def create_file(content, path):
    path.touch()
    file = path.open('w')
    file.write(content)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pyhon project manager')
    parser.add_argument('--package-name', help='package name', required=True)
    parser.add_argument('--user-name', help='User\'s name', required=True)
    parser.add_argument('--user-email', help='User\'s email', required=True)
    parser.add_argument('--organisation', help='Github repostiory\'s organisation', required=True)
    parser.add_argument('--repository-name', help='Github repostory name', required=True)
    parser.add_argument('--verbose', '-v', action='store_true')

    args = parser.parse_args()
    try:
        mapping = args.__dict__
        mkdir(mapping['package_name'])
        env_builder = EnvBuilder()
        env_builder.create(mapping['package_name'])
        package_path = Path(mapping['package_name']) / Path(mapping['package_name'])
        template = get_template('default_package_template')
        content = releif_template(template, mapping)
        create_directory(content, package_path, mapping)
    except Exception as e:
        print('Fail! an error has occured.')
        if args.verbose:
            traceback.print_exception(Exception, e, sys.exc_info()[2])
        else:
            print('Try again with --verbose to see python stack trace.')
