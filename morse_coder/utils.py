from functools import wraps
import time
from rich import print


def timer(func):
    @wraps
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(f"Finished in {stop-start:.3f}s")
        return res

    return wrapper(func)
