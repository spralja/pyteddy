from .. import _db

import sys
from pathlib import Path
import shelve


DB_NAME = str(Path(__file__).parent.parent / 'config')


def execute(**kwargss):
    for kw in kwargss.copy().keys():
        argss = kwargss.pop(kw)
        if argss:
            getattr(sys.modules[__name__], kw)(*argss)

    print(kwargss)


def set_args(*args):
    kwargs = {}
    for arg in args:
        kw, arg = arg.split('=')
        kwargs[kw] = arg

    _db.set(__name__, **kwargs)


def get_args(*kws):
    kwargs = _db.get(__name__, *kws)
    for kw, arg in kwargs.items():
        print('='.join((kw, arg)))
