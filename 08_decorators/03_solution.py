import time

def cache(func):
    cached_agrs = {}
    print(cached_agrs)
    def wrapper(*args):
        if args in cached_agrs:
            return cached_agrs[args]
        result = func(*args)
        cached_agrs[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))