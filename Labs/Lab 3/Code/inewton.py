import numpy as np


def inewton(x_val, y_val, z_val):
    """
    Evaluar el polinomio interpolante P(x)
    usando la formula de Newton.
    Params:
        - x_val, y_val: pares a interpolar
        - z_val: valores en los que evaluar P
    """
    assert len(x_val) == len(y_val), 'x and y must have the same lenght'
    x_val = np.array(x_val, np.float32)
    y_val = np.array(y_val, np.float32)
    m = len(x_val)
    n = m - 1

    # define the matrix F: n x n
    F = np.copy(y_val)
    for k in range(1, m):
        num = (F[k:m] - F[k - 1])
        den = (x_val[k:m] - x_val[k - 1])
        F[k:m] = num / den

    # define the polynomial
    def P(x):
        p = F[n]
        for k in range(1, m):
            p = F[n - k] + (x - x_val[n - k])*p
        return p

    w = [P(z) for z in z_val]
    return w
