from Kernel import *
import numpy as np
from functools import reduce

def make_kernel_smoother(xs, ys, bandwidth, kernel):
    '''
    xs: matrix of x
    ys: matrix of y
    bandwidth: number, self-defined width
    kernel: function, self-defined kernel function
    return: estimated value
    '''
    xs, ys = np.matrix(xs), np.matrix(ys)
    def h(x):
        '''
        x: matrix of x that we observe and want to estimate its f(x)
        return: function
        '''
        x = np.matrix(x)
        if bandwidth < 0:
            return "The bandwidth cannot be negative"
        else:
            w = list(map(kernel, (xs - x) / bandwidth))
            denominator = reduce(lambda x, y: x + y, w)
            nominator = reduce(lambda x, y: x + y, map(lambda x, y: x * y, w, ys))
            if denominator == 0:
                return "The data is not enough to make an estimation"
            else:
                estimate = nominator / denominator
                return estimate.tolist()[0][0]
    return h

def smoother_factory(xs, ys, kernel):
    '''
        xs: matrix of x
    ys: matrix of y
    kernel: function, self-defined kernel function
    return: estimated value
    '''
    xs, ys = np.matrix(xs), np.matrix(ys)
    def g(bandwidth):
        '''
        bandwidth: number, self-defined width
        return: function
        '''
        def h(x):
            '''
            x: matrix of x that we observe and want to estimate its f(x)
            return: function
            '''
            x = np.matrix(x)
            if bandwidth < 0:
                return "The bandwidth cannot be negative"
            else:
                w = list(map(kernel, (xs - x)/bandwidth))
                denominator = reduce(lambda x,y : x+y, w)
                nominator = reduce(lambda x,y : x+y, map(lambda x,y : x*y, w, ys))
                if denominator == 0:
                    return "The data is not enough to make an estimation"
                else:
                    estimate = nominator / denominator
                    return estimate.tolist()[0][0]
        return h
    return g
