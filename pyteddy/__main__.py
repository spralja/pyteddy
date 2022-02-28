from . import __version__
from ._parser import parser

margs = ('version',)
mkwargs = {}
gargs = ('verbose',)
gkwargs = {}

def execute(kwargs):
    if kwargs['version']:
        print('v' + __version__)
    elif not kwargs.get('command'):
        parser.parse_args(['-h'])
        
    exit()


def main():
    kwargs = vars(parser.parse_args())

    for garg in gargs:
        gkwargs[garg] = kwargs.pop(garg)

    for marg in margs:
        mkwargs[marg] = kwargs.pop(marg)

    execute(mkwargs)


if __name__ == '__main__':
    main()
