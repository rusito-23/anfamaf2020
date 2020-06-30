""" Ejercicio 2 """

import numpy as np


""" Helpers """


def soltrinf(A, b):
    """ 
    Solución de un sistema con Ax = b,
    con A triangular inferior no singular.
    """
    
    assert np.linalg.det(A) != 0, 'A no puede ser singular'
    assert A.shape[0] == b.shape[0], 'A y b deben tener la misma altura'
    assert A.shape[0] == A.shape[1], 'A debe ser cuadrada'
    
    # definimos N en base a la dimensión de la matriz A
    N = A.shape[0]
    
    # caculamos el x
    x = np.zeros_like(b, dtype=np.float)
    for i in range(N):
        # buscamos la suma de los productos
        # entre la sección triangular inferior
        # y lo que calculamos ya de X
        s = sum([A[i, j] * x[j] for j in range(i)])
        
        # buscamos el resultado final de x[i]
        x[i] = (b[i] - s) / A[i, i]
        
    return x


""" Ejercicio a) """

def gseidel(A, b, err, mit):
    """
    Solución de un sistema con Ax = b, usando el método de Gauss-Siedel.
    """

    assert np.linalg.det(A) != 0, 'A no puede ser singular'
    assert A.shape[0] == b.shape[0], 'A y b deben tener la misma altura'
    assert A.shape[0] == A.shape[1], 'A debe ser cuadrada'

    # convertimos todo a flotante
    A = A.astype(np.float)
    b = b.astype(np.float)
    
    # inicializamos x con ceros y definimos N
    x = np.zeros_like(b)
    N = A.shape[0]

    # definimos la descomposición A = D + L + U
    D = np.diagflat(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    # matrices a usar en las iteraciones
    M = L + D
    N = U
    
    for k in range(mit):
        
        # buscamos una nueva aproximación
        # buscando la solución: Lu = b - Ux con soltrinf
        u = soltrinf(M, b - np.dot(N, x))
        
        # validamos y actualizamos x
        if (np.abs(u - x) < err).all():
            return u, k
        
        x = u
    
    return x, mit


""" Ejercicio a) """


def sor(A, b, omega, err, mit):
    """
    Solución de un sistema con Ax = b, usando el método de SOR.
    Este caso es muy parecido al anterior, sólo que debemos
    utilizar la variable `omega` como factor de relajación.
    """
    assert np.linalg.det(A) != 0, 'A no puede ser singular'
    assert A.shape[0] == b.shape[0], 'A y b deben tener la misma altura'
    assert A.shape[0] == A.shape[1], 'A debe ser cuadrada'

    # convertimos todo a flotante
    A = A.astype(np.float)
    b = b.astype(np.float)

    # inicializamos x con ceros y definimos N
    x = np.zeros_like(b)
    N = A.shape[0]

    # definimos la descomposición A = D + L + U
    D = np.diagflat(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    # matrices a usar en las iteraciones
    M = (L * omega) + D
    N = (U * omega) + ((omega - 1) * D)
    
    for k in range(mit):
        
        # buscamos una nueva aproximación
        # buscando la solución: Lu = b - Ux con soltrinf
        u = soltrinf(M, (b * omega) - np.dot(N, x))
        
        # validamos y actualizamos x
        if (np.abs(u - x) < err).all():
            return u, k
        
        x = u
    
    return x, mit
    


""" main """


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    # definimos un sistema conocido para probar
    # solución:  (1., -3, -2, 1)
    # construir las matrices
    A = np.stack([[6, -2, 2, 4],
                  [12, -8, 6, 10],
                  [3, -13, 9, 3],
                  [-6, 4, 1, -18]])
    b = np.array([12, 34, 27, -38])

    # probamos el método gsiedel
    x, k = gseidel(A, b, 0.0001, 1000)
    print('Ejercicio a) \n'
          f'- x: {x}\n '
          f'- k: {k}')

    # probamos el método sor
    x, k = sor(A, b, 1.2, 0.001, 1000)
    print('Ejercicio b) \n'
          f'- x: {x}\n '
          f'- k: {k}')
