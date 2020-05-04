"""
Ejercicio 1:

Escribir una función `fibonacci`,
que tome como parámetro un número entero 'n'
y devuelva una lista con los primeros n elementos
de la sucesión de Fibonacci.
"""


def fibonacci(n):
    """
    Fibonacci:
    Params:
        - n: número entero > 0
        - [n]: primeros n elementos de la sucesión
    """
    assert type(n) == int and n >= 1,\
            'La secuencia de Fibonacci sólo es válida'\
                   ' para números mayores o iguales a 1.'
    # inicializar los valores iniciales de la sucesión
    fib = [0, 1]
    for i in range(2, n):
        # fib(n) = fib(n-2) + fib(n-1)
        fib.append(fib[i-2] + fib[i-1])
    return fib


def test_fibonacci(n):
    """
    Testear la función `fibonacci` en un número n.
    """
    fib = fibonacci(n)
    for i in range(2, n):
        assert fib[i] == fib[i-2] + fib[i-1],\
                f'Test de fibonacci falló: {fib[i]} != {fib[i-2]} + {fib[i-1]}'


if __name__ == '__main__':
    # mostrar secuencia de fibonacci
    # para los primeros 10 n
    print('\nEJERCICIO 1:\n')
    fib_10 = fibonacci(10)
    print('Primeros 10 de la secuencia de Fibonacci:\n', fib_10)

    # testear para todos los números hasta 100
    for n in range(100):
        test_fibonacci(100)
