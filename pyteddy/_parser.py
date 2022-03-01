from . import _db

import argparse



def _get_parser():
    HasGargs = argparse.ArgumentParser(add_help=False)
    HasGargs.add_argument('--verbose', '-v', action='store_true', help='show verbose error messages')

    parser = argparse.ArgumentParser(prog='pyteddy', description='python project manager', parents=[HasGargs])
    parser.add_argument('--version', '-V', action='store_true', help='print version')
    command_parsers = parser.add_subparsers(dest='command')

    config_parser = command_parsers.add_parser('config', parents=[HasGargs])
    config_subparser = config_parser.add_subparsers()

    config_set_parser = config_subparser.add_parser('set', parents=[HasGargs])
    config_set_parser.add_argument('set', nargs='+')

    config_get_parser = config_subparser.add_parser('get', parents=[HasGargs])
    config_get_parser.add_argument('get', nargs='+')

    return parser


parser = _get_parser()