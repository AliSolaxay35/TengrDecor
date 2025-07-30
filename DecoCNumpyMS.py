def check_shape(expected_shape):
    def decorator(func):
        def wrapper(matrix, *args, **kwargs):
            if matrix.shape != expected_shape:
                raise ValueError(f"Matrix must have shape {expected_shape}")
            return func(matrix, *args, **kwargs)
        return wrapper
    return decorator

@check_shape((2, 2))
def determinant(mat):
    return np.linalg.det(mat)

import numpy as np
print(determinant(np.array([[1, 2], [3, 4]]))) 
