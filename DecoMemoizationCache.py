cache = {}

def memoize(func):
    def wrapper(x):
        if x in cache:
            print("Using cached value")
            return cache[x]
        result = func(x)
        cache[x] = result
        return result
    return wrapper

@memoize
def expensive_computation(x):
    print("Computing...")
    return np.sqrt(x ** 2 + 5)

import numpy as np
print(expensive_computation(10))
print(expensive_computation(10))  # Cached 
