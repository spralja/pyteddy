from ._parser import parser

gargs = ('verbose',)
gkwargs = {}

def execute(kwargs):
    from .index import execute

    execute(kwargs)


def main():
    kwargs = vars(parser.parse_args())
    
    for garg in gargs:
        gkwargs[garg] = kwargs.pop(garg)

    execute(kwargs)


if __name__ == '__main__':
    main()
