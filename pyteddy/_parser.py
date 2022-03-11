from . import _db

import argparse



def _get_parser():
    HasGargs = argparse.ArgumentParser(add_help=False)
    HasGargs.add_argument('--verbose', '-v', action='store_true', help='show verbose error messages')

    parser = argparse.ArgumentParser(prog='pyteddy', description='python project manager', parents=[HasGargs])
    parser.add_argument('--version', '-V', action='store_true', help='print version')
    command_parsers = parser.add_subparsers(dest='command')


    config_parser = command_parsers.add_parser('config', parents=[HasGargs])
    config_subparsers = config_parser.add_subparsers()

    config_set_parser = config_subparsers.add_parser('set', parents=[HasGargs])
    config_set_parser.add_argument('set', nargs='+')

    config_get_parser = config_subparsers.add_parser('get', parents=[HasGargs])
    config_get_parser.add_argument('get', nargs='+')

    config_del_parser = config_subparsers.add_parser('delete', parents=[HasGargs])
    config_del_parser.add_argument('delete', nargs='+')


    template_parser = command_parsers.add_parser('template', parents=[HasGargs])
    template_subparsers = template_parser.add_subparsers(dest='subcommand')

    template_load_parser = template_subparsers.add_parser('load', parents=[HasGargs])
    template_load_parser.add_argument('name')
    template_load_parser.add_argument('path')

    template_create_parser = template_subparsers.add_parser('create', parents=[HasGargs])
    template_create_parser.add_argument('name')
    template_create_parser.add_argument('path')
    template_create_parser.add_argument('context', nargs='*')

    template_delete_parser = template_subparsers.add_parser('delete', parents=[HasGargs])
    template_delete_parser.add_argument('name')

    return parser


parser = _get_parser()