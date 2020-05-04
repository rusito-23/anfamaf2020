"""
Ejercicio 3
"""
import numpy as np
import matplotlib.pyplot as plt
from ilagrange import ilagrange

"""
Definimos una función para encontrar la enésima derivada
de cos(x), sabiendo que las derivadas siempre siguen:
cos / -sen / -cos / sen
"""

def cos_dx(n, x):
    idx = n % 4
    if (idx == 0): return np.cos(x)
    elif (idx == 1): return -np.sin(x)
    elif (idx == 2): return -np.cos(x)
    else: return np.sin(x)

"""
A)
Definir la función `error_cos(I, n)`, que estime el error máximo
de aproximar la función `cos(x)` usando el polinomio interpolante de Lagrange,
en el intervalo `I = [a, b]` y `n` será la cantidad de puntos interpolantes
(equidistantes) del intervalo `I`.
"""

def error_cos(I, n):
    # assert parameters
    assert isinstance(n, int), 'El parámetro n debe ser entero'
    assert hasattr(I, '__iter__') and len(I) == 2,\
            'El parámetro I debe ser una lista o tupla de dos elementos.' 

    # definimos los n puntos de x
    x_space = np.linspace(*I, n)

    # calculamos n factorial
    prod_n = np.math.factorial(n)
    assert prod_n != 0, 'la cantidad de puntos no permite calcular el factorial'

    # acotamos la derivada enésima del coseno
    # sobre el factorial de n
    max_cos_dx = max([abs(cos_dx(n, x)/prod_n) for x in x_space])

    # contruimos el polinomio a acotar
    # es decir prod((x - x_i)) usando los x_i
    # que construyen el polinomio de Lagrange
    poly = np.poly1d(x_space, True)

    # tomamos los puntos criticos
    # buscando las raices de su derivada
    # ubicados en nuestro intervalo
    critic = poly.deriv().roots
    critic = critic[critic.imag == 0].real
    a, b = I
    critic = [c for c in critic if a < c  and c < b]

    # buscamos el punto critico que maximiza
    # el polinomio
    max_bound = max([abs(poly(c)) for c in critic])

    # finalmente devolvemos la cota
    return abs(abs(max_bound) * abs(max_cos_dx))

"""
B)
Encontrar mediante un bucle que comienze en 2, la cantidad
de puntos que se necesitan en el intervalo `[0, 1]`
para que el error sea menor a 10^(-6).
"""

def punto_b():
    tol = pow(10, (-6))
    I, n = [0, 1], 2
    err = np.inf
    mit = 500

    for _ in range(mit):
        err = error_cos(I, n)
        if err < tol:
            break
        n += 1

    print(f'Se necesitan como mínimo {n} puntos con error: {err}.')

    # ploteamos resultados con n + 1 puntos
    # para ver la caida del error
    f, ax = plt.subplots(n)
    for i, axc in enumerate(ax):
        i += 2
        x = np.linspace(*I, i)
        y = np.cos(x)
        z = np.linspace(*I, n*2)
        w = ilagrange(x, y, z)
        axc.plot(z, w, label=f'ilagrange i {i}, err {error_cos(I, i):.10f}')
        axc.plot(z, np.cos(z), label='cos(x)')
        axc.legend()
    plt.show()


if __name__ == '__main__':
    print('\nPUNTO B:\n')
    punto_b()
