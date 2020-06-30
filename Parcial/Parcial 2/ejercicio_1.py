""" Ejercicio 1) """

import ipdb
import numpy as np
import scipy as sc
import scipy.interpolate
import matplotlib.pyplot as plt


""" Ejercicio a) """


def spline_velocidad(ts, vs):
    """ Realizar un spline cúbico usando los puntos intermedios de ts """

    # preparamos el spline cúbico con los datos dados:
    cs = sc.interpolate.CubicSpline(ts, vs)

    # generamos los x a usar como sample
    # es decir, incluyendo los puntos intermedios de cada par
    midpoints = ts[:-1] + np.diff(ts)/2
    xs = np.sort(np.concatenate((ts, midpoints)))

    # aplicamos el spline 
    ys = cs(xs)

    return xs, ys


""" Ejercicio b) """


def trapecio(a, b, fa, fb):
    """ Regla del Trapecio """
    s = ((b - a) / 2.0) * (fa + fb)
    return s


def trapecio_adaptativo(ts, vs):
    """ Trapecio compuesta para puntos no equidistantes """
    s = 0.0
    for i in range(len(ts) - 1):
        # buscamos los pares a evaluar
        a, b = ts[i], ts[i + 1]
        fa, fb = vs[i], vs[i + 1]

        # acumulamos la aproximación de la integral
        # en el intervalo (a, b)
        s += trapecio(a, b, fa, fb)
    return s


""" Ejercicio c) """


def posicion_particula(ts, vs):
    """ Graficar la posición de la particula """

    # usamos el spline
    xs, ys = spline_velocidad(ts, vs)

    # buscamos la integral entre 0 y cada punto dado por el ej a)
    ps = [ trapecio_adaptativo(xs[:i], ys[:i])
           for i in range(1, len(xs) + 1) ]

    # graficamos la posición en cada punto
    return xs, ps


""" main """


if __name__ == '__main__':

    # inicializamos la tabla de velocidades de la partícula
    ts = np.array([0, 0.22, 0.85, 1, 1.5, 1.6, 1.99])
    vs = np.array([0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01])

    # graficamos resultados del ejercicio a)
    xs, ys = spline_velocidad(ts, vs)
    plt.title('Ejercicio a) - resultado del spline')
    plt.scatter(xs, ys, color='tomato', label='spline')
    plt.scatter(ts, vs, color='dodgerblue', label='original')
    plt.show()

    # graficamos resultados del ejercicio c)
    xs, ps = posicion_particula(ts, vs)
    plt.title('Ejercicio c) - posición de la particula en el tiempo')
    plt.plot(xs, ps, color='dodgerblue')
    plt.show()
