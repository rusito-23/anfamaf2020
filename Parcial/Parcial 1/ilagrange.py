import numpy as np


def ilagrange(x_val, y_val, z_val):
    """
    Evaluar el polinomio interpolante P(x)
    usando la formula de Lagrange.
    Params:
        - x_val, y_val: pares a interpolar
        - z_val: valores en los que evaluar P
    """
    assert len(x_val) == len(y_val), 'x and y must have the same lenght'

    # define the L_k function
    def L(k, x):
        # define the x's without the x_k
        _x_val = [x for i, x in enumerate(x_val) if i != k]
        # numerator (using x = z_i)
        num = [(x - x_i) for x_i in _x_val]
        # denominator (using x_k)
        den = [(x_val[k] - x_i) for x_i in _x_val]
        return np.prod(num)/np.prod(den)

    # define the polynomial
    def P(x):
        # the sum L_k(x)*f(x_i)
        s = [L(k, x)*y for k, y in enumerate(y_val)]
        return sum(s)

    w = [P(z) for z in z_val]
    return w
