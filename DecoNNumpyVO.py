import numpy as np

def normalize_output(func):
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        norm = np.linalg.norm(output)
        if norm == 0:
            return output
        return output / norm
    return wrapper

@normalize_output
def get_random_vector():
    return np.random.rand(3)

print(get_random_vector()) 

