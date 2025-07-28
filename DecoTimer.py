import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer
def compute():
    total = sum(range(10**6))
    return total

compute() 
