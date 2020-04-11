

def horn(coefs, x):
    """
    Usa el método de Horner:
    https://en.wikipedia.org/wiki/Horner%27s_method
    Para evaluar un polinomio de grado n (len(coefs))
    en un valor de x (x).
    Los coefiecientes de reciben ordenados de mayor a menor.
    """
    p = coefs[0]
    for c in coefs[1:]:
        p = (p * x) + c
    return p
