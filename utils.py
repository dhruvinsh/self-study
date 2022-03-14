"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

collection of some utility functions that helps to execute/write code better.
"""

import time
from functools import wraps

def time_it(func):
    """allow to calculate execution of given function.

    Args:
        func (Any): function get passed here

    Returns:
        evaluate main funciton and return that.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, *kwargs)
        end = time.time()
        print(f"Function: {func.__name__} took: {end - start:.2f} sec")
        return ret
    return inner
