import numpy as np
import sys


def get_overflow():
    overflow = 2.
    while not np.isinf(overflow*2.):
        overflow *= 2.
    return overflow


def get_underflow():
    underflow = 1
    while not underflow/2 == 0:
        underflow /= 2
    return underflow


if __name__ == '__main__':
    print(f'Overflow is: {get_overflow()}')
    print(f'Underflow is: {get_underflow()}')
    print(f'Sys Overflow is: {sys.float_info.max}')
    print(f'Sys Underflow is: {sys.float_info.min}')
