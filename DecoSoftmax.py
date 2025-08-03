def softmax_output(func):
    def wrapper(*args, **kwargs):
        logits = func(*args, **kwargs)
        exps = np.exp(logits - np.max(logits))
        return exps / np.sum(exps)
    return wrapper

@softmax_output
def model_output():
    return np.array([2.0, 1.0, 0.1])

import numpy as np
print(model_output()) 
