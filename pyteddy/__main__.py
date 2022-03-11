from . import _db, __version__
from ._parser import parser

import sys
import traceback

gargs = ('verbose',)
gkwargs = {}

def execute(kwargs):
    from .commands import execute

    execute(kwargs)


def main():
    kwargs = vars(parser.parse_args())
    print(kwargs)
    verbose = kwargs.pop('verbose')

    if kwargs.pop('version'):
        print(f'v{__version__}')
        exit()

    try: 
        execute(kwargs)
    except Exception as e:
        print('Error: an error has accoured')
        if verbose:
            traceback.print_exception(e, e, sys.exc_info()[2])
        else:
            print('add --verbose to print python stack trace')


if __name__ == '__main__':
    main()
