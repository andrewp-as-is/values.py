__all__ = ['get']


import collections.abc


def _iterable(obj):
    return isinstance(obj, collections.abc.Iterable)


def _string(value):
    try:
        return isinstance(value, basestring)
    except NameError:
        return isinstance(value, str)


def get(input):
    """return a list with input values or [] if input is None"""
    if input is None:
        return []
    if not _iterable(input) or _string(input):
        return [input]
    return list(input)
