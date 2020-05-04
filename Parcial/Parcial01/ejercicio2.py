"""
Ejercicio 2
"""
import itertools
import warnings
import numpy as np
import matplotlib.pyplot as plt
from rnewton import rnewton
from rsteff import rsteff

# no mostrar los runtime warnings
warnings.filterwarnings('ignore')

"""
Definimos las funciones que vamos a necesitar:
función a trabajar: `f(x) = log(x) - 1/x`
derivada: `f'(x) = (x + 1) / x^2`
función de iteración para steff: `g(x) = x - f(x)^2 / f(x + f(x)) - f(x))`
función parámetro para el método de Netwon: `rnewton_fun`
    que devuelve el par `f(x), f'(x)`
función parámetro para el método de Steffensen: `rsteff_fun`
    que devuelve el par `f(x), g(x)`
"""

f = lambda x: np.log(x) - 1/x
f_p = lambda x: (x + 1)/pow(x, 2)
g = lambda x: x - (pow(f(x), 2) / (f(x + f(x)) - f(x)))

rnewton_fun = lambda x: (f(x), f_p(x))
rsteff_fun = lambda x: (f(x), g(x))

"""
Definimos los parámetros dados por el ejercicio.
"""

err = pow(10, -6)
mit = 100

"""
A)
Considerando la función `f(x) = log(x) - 1/x`, estimar la raiz
usando el método de Netwon, con punto inicial `x0 = 1.4`,
máximo número de iteraciones `100` y tolerancia `10^(-6)`.
"""

def punto_a():
    hx, hf = rnewton(rnewton_fun, 1.4, err, mit)
    print('El resultado del punto a (método de Newton) es: \n'
          f'f({hx[-1]:.10f}) = {hf[-1]:.10f} \n'
          'Vemos que es correcto, ya que tenemos una diferencia de '
          'menos de 6 decimales.')

"""
B)
Estimar las raices del punto anterior, usando el método de Steffensen,
con los mismos parámetros.
"""

def punto_b():
    hx, hf = rsteff(rsteff_fun, 1.4, err, mit)
    print('El resultado del punto b (método de Steffensen) es: \n'
          f'f({hx[-1]:.10f}) = {hf[-1]:.10f} \n'
          'Vemos que es correcto, ya que tenemos una diferencia de '
          'menos de 6 decimales.')

"""
C)
Comparar ambos métodos, variando el punto inicial
x0 entre `[1.39, 1.4, 1.41, 3]` y dar una breve conclusión
los beneficios de cada método.
"""

def punto_c():
    # incializar los parámetros a comparar
    # y crear la lista tuplas con las combinaciones a comparar
    initials = [1.39, 1.4, 1.41, 3.]
    methods = [(rnewton, rnewton_fun), (rsteff, rsteff_fun)]
    combinations = list(itertools.product(initials, methods))

    # evaluar las combinaciones y guardar los resultados
    # los resultados serán tuplas de la forma:
    # (nombre del método, punto inicial, x calculados, estimaciones de cero)
    results = []
    for x0, (method, fun) in combinations:
        hx, hf = method(fun, x0, err, mit)
        results.append((method.__name__, x0, hx, hf))
        print(f'Método {method.__name__} '
              f'\tx0 = {x0} '
              f'\tResultados: x {hx[-1]:.7f}\t f(x) {hf[-1]:.7f} '
              f'\t {len(hx)} iteraciones')

    # crear un gráfico para mostrar los resultados
    fig, ax = plt.subplots(len(initials), len(methods), figsize=(15, 15))
    ax = ax.ravel()

    for axc, (method, x0, hx, hf) in zip(ax, results):
        axc.set_title(f'{method} using x0 = {x0}')
        # graficar las estimaciones
        axc.scatter(hx, hf, label=f'estimaciones ({len(hx)})', color='orange')
        # graficar la función original
        hxs = np.linspace(min(hx), max(hx), 1000)
        axc.plot(hxs, [f(x) for x in hxs], label='f(x)')
        # centrar el gráfico en cero si la estimación no falló
        failed = not any(abs(f_x) < abs(err) for f_x in hf)
        if not failed:
            axc.spines['left'].set_position('center')
            axc.spines['bottom'].set_position('zero')
            axc.spines['right'].set_color('none')
            axc.spines['top'].set_color('none')
            # mostrar el zero con un color distinto
            axc.scatter(hx[-1], hf[-1], label='zero', color='red')
        axc.legend()
    plt.show()

"""
Conclusión:
    por lo que se puede observar en los gráficos y los resultados,
    ambos métodos utilizan la misma cantidad de iteraciones.
    Uno de los puntos a favor del método de Steffensen es que no
    necesitamos tener la derivada de la función en cuestión.
    Sin embargo, como el método de Steffensen utiliza una función
    de iteración, puede fallar en algunos valores.
    En el último caso que probamos, se ve que falla por querer
    tomar el log de un número negativo.
"""

"""
PRINCIPAL:
Correr todos los puntos del ejercicio.
"""

if __name__ == '__main__':
    print('\n PUNTO A: \n')
    punto_a()

    print('\n PUNTO B: \n')
    punto_b()

    print('\n PUNTO C: \n')
    punto_c()
