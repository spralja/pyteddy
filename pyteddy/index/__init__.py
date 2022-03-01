from .. import __version__

import sys
import importlib

def execute(kwargs):
    if kwargs.pop('version'):
        print('v' + __version__)
        exit()

    command = kwargs.pop('command')

    if command is None:
        raise TypeError('not command')
        
    importlib.__import__('.'.join((__package__, command)) , fromlist=('execute'))
    getattr(sys.modules[__name__], command).execute(**kwargs)
