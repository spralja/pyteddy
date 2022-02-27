from . import get_template
from .templates import releif_template
from . import commands

import argparse
import sys
import traceback


VERSION = '0.0.2'


def match(command, *args, **kwargs):
    try:
        return getattr(sys.modules[commands.__name__], command.replace('-', '_'))
    except:
        print('unknown command')
        sys.exit(1)

def version(*args, **kwargs):
    print('v' + VERSION)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pyteddy', description='pyhon project manager')
    parser.add_argument('--version', '-v', help='get version', action='store_true')
    subparsers = parser.add_subparsers(help='subparsers', dest='command')
    create_package_parser = subparsers.add_parser('create-package', help='creates a package')
    create_package_parser.add_argument('--package-name', help='package name', required=True)
    create_package_parser.add_argument('--user-name', help='User\'s name', required=True)
    create_package_parser.add_argument('--user-email', help='User\'s email', required=True)
    create_package_parser.add_argument('--organisation', help='Github repostiory\'s organisation', required=True)
    create_package_parser.add_argument('--repository-name', help='Github repostory name', required=True)
    create_package_parser.add_argument('--verbose', '-v', help='enable verbose error messages', action='store_true')
    create_package_parser.add_argument('--year', '-y', help='year used to releif template')

    args = parser.parse_args()

    verbose = False
    if vars(args).get('verbose'):
        verbose = True
        vars(args).pop('verbose')

    try:
        if vars(args).get('version'):
            vars(args).pop('version')
            version()
        elif args.command is None:
            parser.parse_args(['--help'])
        else:
            match(args.command)(args)
    except Exception as e:
        print('Fail! an error has occured.')
        if verbose:
            traceback.print_exception(Exception, e, sys.exc_info()[2])
        elif type(e) is FileExistsError:
            print('directory already exsists')
        else:
            print('Try again with --verbose to see python stack trace.')
