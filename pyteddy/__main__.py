from . import _db, CARGS
from ._parser import parser

import sys
import traceback

gargs = ('verbose',)
gkwargs = {}

def execute(kwargs):
    from .index import execute

    execute(kwargs)


def main():
    kwargs = vars(parser.parse_args())
    
    for garg in gargs:
        gkwargs[garg] = kwargs.pop(garg)
        if garg in CARGS:
            carg = _db.get('config').get(garg)
            if carg:
                gkwargs[garg] = carg
    try: 
        execute(kwargs)
    except Exception as e:
        print('Error: an error has accoured')
        if gkwargs['verbose']:
            traceback.print_exception(e, e, sys.exc_info()[2])
            if gkwargs['verbose'] is True:
                print('remove --verbose to supress printing python stack trace')
            else:
                print(f"python stack trace is printing because verbose is set to {gkwargs['verbose']!r} in config,\nrun \'pyteddy config del verbose\' to remove it from config")
        else:
            print('add --verbose to print python stack trace')


if __name__ == '__main__':
    main()
