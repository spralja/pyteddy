import argparse


def _get_parser():
    HasGargs = argparse.ArgumentParser(add_help=False)
    HasGargs.add_argument('--verbose', '-v', action='store_true', help='show verbose error messages')
    HasGargs.add_argument('--debug', '-d', action='store_true', help='show debug information')

    parser = argparse.ArgumentParser(prog='pyteddy', description='python project manager', parents=[HasGargs])
    parser.add_argument('--version', '-V', action='store_true', help='print version')
    command_parsers = parser.add_subparsers(dest='command')

    config_parser = command_parsers.add_parser('config', parents=[HasGargs])
    config_parser.add_argument('--set', '-s', nargs='+')
    config_parser.add_argument('--get', '-g', nargs='+')

    return parser


parser = _get_parser()