import math


def mala(a, b, c):
    """
    Encontrar soluciones de una ecuación de segundo grado.
    Usa la fórmula estándar.
    """
    x_1 = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
    x_2 = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)
    return x_1, x_2


def buena(a, b, c):
    """
    Busca las soluciones de una ecuación de segundo grado.
    No busca raices imaginarias y calcula primero la raiz
    que esté más lejos del cero, para evitar problemas de
    representación de números flotantes.
    """
    # avoid math errors
    if (b ** 2 - 4 * a * c) < 0:
        print('No real solution available')
        return None

    # get the farest root from zero
    if b >= 0:
        x_1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    else:
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    # avoid division by zero
    # if one of the roots is zero,
    # let's assume they both are
    if x_1 == 0:
        return 0, 0

    x_2 = c / (a * x_1)
    return x_1, x_2
