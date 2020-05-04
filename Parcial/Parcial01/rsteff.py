def rsteff(fun, x0, err, mit):
    """
    Usa el método de Steffenson para estimar las raices de una función.
    Params:
        - fun: función que devuelve los valores (f(x), g(x)), donde
            g(x) es la función de iteración.
        - x0: valor inicial
        - err: error tolerable
        - mit: cantidad máxima de iteraciones
    Returns: hx, hf donde:
        - hx es el historial de puntos que se evaluaron
        - hf es el historial de valores de la función en dichos puntos
    """
    hx, hf = [], []
    p0 = x0


    assert isinstance(x0, float), 'El punto inicial debe ser de punto flotante.'
    assert isinstance(mit, int), 'La cantidad máxima de iteraciones debe ser entera.'
    assert callable(fun), 'El parámetro fun debe ser una función'


    for _ in range(mit):
        # buscar los primeros dos términos
        _, p1 = fun(p0)
        _, p2 = fun(p1)

        # aplicar el método de Aitken
        p = p0 - (pow((p1 - p0), 2) / (p2 - 2*p1 + p0))

        # guardar resultados parciales
        hx.append(p), hf.append(fun(p)[0])

        # cortar si hay una solución aceptable
        if abs(p - p0) < err:
            break

        # actualizamos p0 para la siguiente iteración
        p0 = p

    return hx, hf
