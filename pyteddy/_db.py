import shelve


def set(name, **kwargs):
    with shelve.open(name) as db:
        for kw in kwargs.copy().keys():
            db[kw] = kwargs[kw]


def get(name, *kws):
    kwargs = {}
    with shelve.open(name) as db:
        for kw in kws:
            kwargs[kw] = db[kw]

    return kwargs
