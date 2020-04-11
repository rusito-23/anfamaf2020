import math
import matplotlib.pyplot as plt
import numpy as np


def rbisec(fun, I, err, mit):
    """
    Usa el método de bisección
    https://en.wikipedia.org/wiki/Bisection_method
    para encontrar una aproximación del valor
    donde la función dada es cero.
    Params:
        - fun: función a evaluar
        - I: intervalo de evaluación
        - err: error tolerable
        - mit: cantidad máxima de iteraciones
    Returns: hx, hf donde:
        - hx es el historial de puntos que se evaluaron
        - hf es el historial de valores de la función en dichos puntos
    """
    a, b = I
    hm, hf = [], []

    for _ in range(mit):
        # get midpoint
        m = (a + b) / 2

        # save partial results
        hm.append(m)
        hf.append(fun(m))

        # check results using the abs error
        if (abs(fun(m)) < abs(err)):
            break

        # find the new interval
        if fun(a)*fun(m) < 0:
            b = m
        elif fun(b)*fun(m) < 0:
            a = m

    return hm, hf


def plot_bisec(fun, I, err, mit, figsize=5):
    """
    Función útil para plotear resultados dados
    por la función `bisec`.
    Plotea tanto los valores reales de la función,
    como los valores del historial dado por bisec
    """

    # create the samples
    I_x = [np.linspace(*i, 1000) for i in I]

    # get the real values
    I_r = [np.array([
        fun(x)
        for x in I_s
    ]) for I_s in I_x]

    # get our own results using bisec
    I_b = [
        rbisec(fun, i, err, mit)
        for i in I
    ]

    # create the fig and axes
    fig, ax = plt.subplots(1, len(I), figsize=(figsize*len(I), figsize))

    # for each ax
    for i, (ii, x, r, (hx, hf)) in enumerate(zip(I, I_x, I_r, I_b)):
        ax[i].set_title(f'I{i}: {ii}')

        # show the real results
        ax[i].plot(x, r, label='f(x)')

        # show the results using bisec
        bis_failed = not any(abs(f_x) < abs(err) for f_x in hf)
        # check if the bisc failed (not close enough to zero)
        if bis_failed:
            centerx = sum(ii)/2
            centery = ax[i].get_yticks()[3]
            ax[i].text(centerx, centery, 'BISEC FAILED',
                       horizontalalignment='center',
                       verticalalignment='center',
                       color='red')
        else:
            # bisec didn't failed, show results
            ax[i].scatter(hx, hf, label='bisec(I)', color='orange')
            # center the zero
            ax[i].spines['left'].set_position('center')
            ax[i].spines['bottom'].set_position('zero')
            # show zero in another color
            ax[i].scatter(hx[-1], hf[-1], label='zero', color='red')

        ax[i].spines['right'].set_color('none')
        ax[i].spines['top'].set_color('none')

        ax[i].legend()

    plt.show()


if __name__ == '__main__':

    # plot bisec for tan(x)
    # in intervals: (2, 4) & (5, 7)
    plot_bisec(math.tan, [(2, 4), (5, 7)], pow(10, -5), 100)

    # plot bisex for f(x) = x^2 - 3
    # define our intervals
    plot_bisec(lambda x: pow(x, 2) - 3, [(-3, 3), (6, 90)], pow(10, -5), 100)
