DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def is_iterable(x):
    if isinstance(x, list) or isinstance(x, set) or isinstance(x, tuple):
        return True
    else:
        return False