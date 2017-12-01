from Kernel import *
import numpy as np

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
        return helper(x, xs, ys, bandwidth, kernel)
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
            return helper(x, xs, ys, bandwidth, kernel)
        return h
    return g

def helper(x, xs, ys, bandwidth, kernel):
    '''
    x: matrix of x that we observe and want to estimate its f(x)
    xs: matrix of x
    ys: matrix of y
    bandwidth: number, self-defined width
    kernel: function, self-defined kernel function
    return: function
    '''
    x = np.matrix(x)
    if bandwidth < 0:
        raise ValueError("Bandwidth cannot be negative")
    w = list(map(kernel, (xs - x) / bandwidth))
    denominator = sum(w)
    nominator = (w*ys).tolist()[0][0]
    if denominator == 0:
        raise ValueError("All weights are zero")
    else:
        estimate = nominator / denominator
        return estimate
