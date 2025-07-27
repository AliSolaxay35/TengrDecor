def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(3, 5)) 
