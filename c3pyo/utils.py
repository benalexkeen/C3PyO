def is_iterable(x):
    if isinstance(x, list) or isinstance(x, set) or isinstance(x, tuple):
        return True
    else:
        return False