import numpy as np
from functools import reduce

def GaussianKernel(s):
    '''
    s: matrix
    return: weight
    '''
    s = distance(s)
    return (1/np.sqrt(2*np.pi))*np.exp(-s**2/2)

def BoxcarKernel(s):
    '''
    s: matrix
    return: weight
    '''
    s = distance(s)
    if s <= 1:
        return 1/2
    else:
        return 0

def help(acum, x):
    '''
    acum: initial value
    x: number
    return: acum + x**2
    '''
    return acum + x**2

def distance(s):
    '''
    s: matrix
    return: number as (xs-x)/b
    '''
    s = np.array(s)[0].tolist()
    s = np.sqrt(reduce(help, s, 0))
    return s