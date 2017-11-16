import numpy as np

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

def distance(s):
    '''
    s: vector
    return: number as (xs-x)/b
    '''
    s = np.array(s)
    s = np.sqrt(np.sum(s**2))
    return s
