def positive_args_only(func):
    def wrapper(*args):
        if any(a < 0 for a in args):
            raise ValueError("Negative values are not allowed")
        return func(*args)
    return wrapper

@positive_args_only
def multiply(x, y):
    return x * y

print(multiply(3, 5))
# print(multiply(-1, 2))  # Will raise an error 
