

def ripf(fun, x0, err, mit):
    """
    Usando el método de Iteractión de punto fijo
    https://es.wikipedia.org/wiki/Método_del_punto_fijo
    busca una aproximación del donde f(x) es cero.
    Params:
        - fun: es la función de iteración (i.e: x - f(x))
        - x0: un punto en R
        - err: error tolerable
        - mit: máxima cantidad de iteraciones
    """
    hx = []
    x_k = x0

    for i in range(mit):
        p = fun(x_k)
        hx.append(p)

        if abs(p - x_k) < err:
            break

        x_k = p

    return hx
