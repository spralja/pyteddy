from pathlib import Path
import shelve

DB_NAME = str(Path(__file__).parent / 'db')


def get(command):
    kwargs = {}
    with shelve.open(DB_NAME) as db:
        ckwargs = db[command]

    return ckwargs


def update(command, **kwargs):
    with shelve.open(DB_NAME) as db:
        if db.get(command) is None:
            db[command] = {}

        ckwargs = db[command]
        ckwargs.update(kwargs)
        db[command] = ckwargs
