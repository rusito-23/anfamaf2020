import numpy as np


def fact(n):
    return np.prod(range(1, n+1))


if __name__ == '__main__':
    print(f'Factorial de 6 es: {fact(6)}')
