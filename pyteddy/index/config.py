from .. import _db

from pathlib import Path
import shelve
import sys

COMMAND = Path(__file__).name.split('.')[0]


def execute(**kwargss):
    for kw in kwargss.copy().keys():
        argss = kwargss.pop(kw)
        if argss:
            getattr(sys.modules[__name__], kw)(*argss)


def set(*args):
    kwargs = {}
    for arg in args:
        kw, arg = arg.split('=')
        kwargs[kw] = arg

    _db.update('config', **kwargs)


def get(*kws):
    kwargs = _db.get('config')
    for kw in kws:
        kwarg = kw, kwargs[kw]
        print('='.join(kwarg))
