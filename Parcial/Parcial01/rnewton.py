def rnewton(fun, x0, err, mit):
    """
    Usa el método de Newton para estimar las raices de una función.
    Params:
        - fun: función que devuelve los valores (f(x), f'(x))
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

    assert isinstance(x0, float), 'El punto inicial debe ser de punto flotante.'
    assert isinstance(mit, int), 'La cantidad máxima de iteraciones debe ser entera.'
    assert callable(fun), 'El parámetro fun debe ser una función'

    for _ in range(mit):
        # buscar y guardar resultados parciales
        f_x, f_p_x = fun(x_k)
        hx.append(x_k), hf.append(f_x)

        # cortar si hay una solución aceptable
        if (abs(f_x) < abs(err)):
            break

        # cortar si el resultado actual es insignificante
        # comparado con el anterior
        abs_x_k = abs(x_k - x_k_p)
        if x_k != 0 and (abs_x_k / abs(x_k) < abs(err)):
            break

        # evitar la divisón por cero
        # o bien f(x) es constante
        # o bien tiene un máximo o un mínimo
        if (f_p_x == 0):
            break

        # computar la siguiente aproximación
        x_k_p = x_k
        x_k = x_k - (f_x / f_p_x)

    return hx, hf
