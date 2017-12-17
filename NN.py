import numpy as np

def activation(z, type):

    if type == 'sigmoid':
        A = 1/(1 + np.exp(-z))
    elif type == 'tanh':
        A = 1 - 2*np.exp(-z)/(np.exp(z) + np.exp(-z))
    elif type == 'relu':
        A = z if z > 0 else 0
    return A

def derivative(z, type):

    if type == 'sigmoid':
        d = activation(z, 'sigmoid')*(1 - activation(z, 'sigmoid'))
    elif type == 'tanh':
        d = 1 - activation(z, 'tanh')**2
    elif type == 'relu':
        d = 1
    return d

def initialize(layer_dim):
    np.random.seed(1)

    L = len(layer_dim)
    parameters = {}

    for i in range(1, L):
        parameters['w' + str(i)] = np.random.randn((layer_dim[i], layer_dim[i-1]))*0.01
        parameters['b' + str(i)] = np.zeros((layer_dim[i], 1))

    return parameters

def step_forward(A_pre, w, b, act):
    z = np.dot(w, A_pre) + b

    return z, activation(z, act)

def forward_propagation(X, parameters, types):
    A = X
    L = len(parameters) // 2
    cache = [[0, A]]

    for i in range(1, L+1):
        A_pre = A
        z, A = step_forward(A_pre, parameters['w' + str(i)], parameters['b' + str(i)], types[i-1])
        cache.append([z, A])

    assert(type[-1] == 'sigmoid')

    return cache

def step_backward(X, w_next, dz_next, z_cur, A_last, act):

    m = X.shape[0]

    dz = (1/m)*np.multiply(np.dot(w_next.T, dz_next), derivative(z_cur, act))
    dw = np.dot(dz, A_last.T)
    db = np.sum(dz, axis = 1, keepdims = True)

    gradient = {'dz':dz,
                'dw':dw,
                'db':db}

    return gradient

def backward_propagation(X, y, parameters, types, cache):

    m = X.shape[0]

    gradients = {}
    L = len(parameters) // 2

    for i in range(L, 0, -1):
        if i == L:
            dz = (1/m)*(cache[i][1] - y)
            dw = np.dot(dz, cache[i-1].T)
            db = np.sum(dz, axis = 1, keepdims = True)
            gradients['dz' + str(i)] = dz
            gradients['dw' + str(i)] = dw
            gradients['db' + str(i)] = db
        else:
            w_next = parameters['dw' + str(i+1)]
            dz_next = parameters['dz' + str(i+1)]
            z_cur = cache[i][0]
            A_last = cache[i-1][1]
            act = types[i-1]
            gradient = step_backward(X, w_next, dz_next, z_cur, A_last, act)
            gradients['dz' + str(i)] = gradient['dz']
            gradients['dw' + str(i)] = gradient['dw']
            gradients['db' + str(i)] = gradient['db']
    return gradients

def optimization(X, y, layer_dim, types, iterations, learning_rate):

    parameters = initialize(layer_dim)
    cache = forward_propagation(X, parameters, types)
    L = len(parameters) // 2
    cost = [cache[-1][1]]

    for i in range(iterations):
        gradients = backward_propagation(X, y, parameters, types, cache)
        for j in range(1, L+1):
            parameters['w' + str(i)] = parameters['w' + str(i)] - learning_rate*gradients['dw' + str(i)]
            parameters['b' + str(i)] = parameters['b' + str(i)] - learning_rate*gradients['db' + str(i)]
        cache = forward_propagation(X, parameters, types)
        cost.append(cache[-1][1])

    return cost, parameters
