import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    calculations = {
        'mean' : [numpy.mean(matrix, axis=0).tolist(), numpy.mean(matrix, axis=1).tolist(), numpy.mean(matrix).item()],

        'variance' : [numpy.var(matrix, axis=0).tolist(), numpy.var(matrix, axis=1).tolist(), numpy.var(matrix).item()],

        'standard deviation' : [numpy.std(matrix, axis=0).tolist(), numpy.std(matrix, axis=1).tolist(), numpy.std(matrix).item()],

        'max' : [numpy.max(matrix, axis=0).tolist(), numpy.max(matrix, axis=1).tolist(), numpy.max(matrix).item()],

        'min' : [numpy.min(matrix, axis=0).tolist(), numpy.min(matrix, axis=1).tolist(), numpy.min(matrix).item()],

        'sum' : [numpy.sum(matrix, axis=0).tolist(), numpy.sum(matrix, axis=1).tolist(), numpy.sum(matrix).item()]
    }
    
    return calculations
