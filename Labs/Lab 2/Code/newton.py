

def rnewton(fun, x0, err, mit):
    """
    Usa el método de Newton
    https://en.wikipedia.org/wiki/Newton%27s_method
    para encontrar el punto en el que
    la función dada se hace cero.
    Params:
        - fun: función que devuelve los valores f(x) f'(x)
        - x0: valor inicial
        - err: error tolerable
        - mit: cantidad máxima de iteraciones
    Returns: hx, hf donde:
        - hx es el historial de puntos que se evaluaron
        - hf es el historial de valores de la función en dichos puntos
    """
    x_k_p = 0
    x_k = x0
    hx, hf = [], []

    for _ in range(mit):
        # get partial results
        f_x, f_p_x = fun(x_k)
        hx.append(x_k), hf.append(f_x)

        # have we found the solution?
        if (abs(f_x) < abs(err)):
            break

        # my x_k is not significant
        # compared to my last x_k_p
        abs_x_k = abs(x_k - x_k_p)
        if x_k != 0 and (abs_x_k / abs(x_k) < abs(err)):
            break

        # avoid division by zero
        # either f is constant
        # or has a max / min point
        if (f_p_x == 0):
            break

        # compute next approximation
        x_k_p = x_k
        x_k = x_k - (f_x / f_p_x)

    return hx, hf


def cubic_root(a):
    """
    Dado a > 0, encuentra la raiz cúbica
    usando la aproximación de Newton.
    """
    assert a > 0, 'a must be > 0'

    # define f(x) = x^3 - a,
    # his derivative
    # and the helper function

    def f(x):
        return pow(x, 3) - a

    def f_p(x):
        return 3 * pow(x, 2)

    def fun(x):
        return (f(x), f_p(x))

    # get newton's approximation
    hx, hf = rnewton(fun, a, pow(10, -6), 100)

    print(f'Newton\'s approximation to {a}^(1/3) is {hx[-1]:.2f}')
    return hx[-1]


if __name__ == '__main__':
    cubic_root(27)
    cubic_root(9)
