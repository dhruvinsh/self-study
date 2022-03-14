import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, *kwargs)
        end = time.time()
        print(f"Function: {func.__name__} took: {end - start:.2f} sec")
        return ret
    return inner
