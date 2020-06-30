"""
Ejercicio 3: Programación Lineal
Este ejercicio va a estar centrado en el problema:

maximizar: z = 500x + 300y
sujeto a:
    2x + y <= 40
    x + 2y <= 50

Se va a resolver el problema utilizando el módulo scipy.optimize.
Como éste módulo nos permite únicamente minimizar nuestras variables,
debemos transformar nuestro problema a uno de minimización.
"""

import scipy as sc
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt


""" Ejercicio a) """


def ejercicio_a():
    """
    Usa el módulo scipy.optimize para encontrar la solución al problema.
    """

    # definimos el z a minimizar y las restricciones

    z = lambda x: - ( 500*x[0] + 300*x[1] ) 
    hour_constraint = lambda x: 40 - (2*x[0] + x[1])
    capacity_constraint = lambda x: 50 - (x[0] + 2*x[1])

    constraints =  (
            {'type': 'ineq', 'fun': hour_constraint},
            {'type': 'ineq', 'fun': capacity_constraint})

    # minimizamos

    sol = sc.optimize.minimize(z, (0, 0), constraints=constraints)

    x, y, m = round(sol.x[0]), round(sol.x[1]), -round(sol.fun)
    return x, y, m


""" Ejercicio b) """


def ejercicio_b():
    """
    Muestra el gráfico de la región factible del problema.
    Buscamos la región dada por las restricciones:
        2x + y <= 40
        x + 2y <= 50
    """

    x = np.linspace(0, 23)

    # buscar las rectas que definen nuestras restricciones
    y1 = 40 - 2*x
    y2 = (50 - x) / 2

    # graficar estas rectas
    plt.plot(x, y1, label='y = 40 - 2x')
    plt.plot(x, y2, label='y = (50 - x) * 1/2')

    # graficar el espacio que cumple con todas las condiciones
    plt.fill_between(x, np.minimum.reduce([y1, y2]), 0,
                     alpha=0.7, color='dodgerblue', label='fact region')

    # mostrar también el vector gradiente hacia donde
    # la función de maximiza, para ver gráficamente
    # que la solución dada corresponde con el vértice
    # donde la función de maximiza dentro de la región factible
    plt.quiver(500, 300, color='tomato', label='grad vector')

    plt.xlim(0, 23)
    plt.ylim(0, 46)
    plt.legend()
    plt.show()


"""
Ejercicio c)

En este ejercicio, debemos incluir una nueva variable a nuestro problema,
que son la cantidad de horas trabajadas por nuestro empleado (h).

Vamos a maximizar: z = 500x + 300y - 200h
Sujeto a:
    2x + y <= 40 + h
    x + 2y <= 50
    h <= 40 ----------- (no podemos hacerlo trabajar +40hs semanales)

Si el valor de z maximizado es mayor que el z del ejercicio a), entonces,
nos va a convenir contratar un empleado (con la h dada). De lo contrario,
vamos a tener que trabajar solitos.
"""

def ejercicio_c():

    # definimos el z a minimizar y las restricciones

    z = lambda x: - ( 500*x[0] + 300*x[1] - 200*x[2] ) 
    hour_constraint = lambda x: (40 + x[2]) - (2*x[0] + x[1])
    capacity_constraint = lambda x: 50 - (x[0] + 2*x[1])
    employee_constraint = lambda x: 40 - x[2]

    constraints =  (
            {'type': 'ineq', 'fun': hour_constraint},
            {'type': 'ineq', 'fun': capacity_constraint},
            {'type': 'ineq', 'fun': employee_constraint})

    # minimizamos

    sol = sc.optimize.minimize(z, (0, 0, 0), constraints=constraints)

    x, y, h, m = round(sol.x[0]), round(sol.x[1]),\
                 round(sol.x[2]), -round(sol.fun)
    return x, y, h, m



""" main """


if __name__ == '__main__':

    # ejercicio a
    xa, ya, ma = ejercicio_a()
    print(f'''
    Ejercicio a)
    El carpintero debe fabricar {xa} mesas y {ya} sillas
    para lograr un ingreso máximo de {ma} por semana.
    Esta solución tiene sentido, ya que estos puntos determinan
    un vértice en la región factible.
    ''')

    # ejercicio c
    xb, yb, hb, mb = ejercicio_c()
    print(f'''
    Ejercicio a)
    El carpintero debe fabricar {xb} mesas y {yb} sillas
    con un empleado trabajando {hb} hora
    para lograr un ingreso máximo de {mb} por semana.
    Le conviene? {mb > ma}.''')

    # mostrar region factible
    ejercicio_b()

