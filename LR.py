import numpy as np

def sigmoid(z):
    '''
    z: a matrix
    return: a matrix
    '''
    s = 1/(1 + np.exp(-z))

    asset(s.shape == z.shape)

    return s

def initialize(dim):
    '''
    dim: number of parameters
    return: w and b
    '''

    w = np.zeros((dim, 1))
    b = 0

    assert(w.shape = (dim, 1))
    assert(isinstance(b, int) or isinstance(b, float))

    return w, b

def propagate(w, b, X, y):
    '''
    w: weights, [n 1]
    b: a scaler
    X: a matrix, n parameters and m samples, [n m]
    y: a vector, [m 1]
    return:
    cost: J = 1/m*(sum(-(y*log(a) + (1-y)*log(1-a))))
    dw: a matrix, the derivative of J to w, [n 1]
    db: a scaler, the derivate of J to b
    '''

    m = X.shape[0]
    z = np.dot(w.T, X) + b
    A = sigmoid(z)
    cost = -(1/m)*np.sum(np.multiply(y, np.log(a)) + np.multiply(1-y, np.log(1-a)))

    dw = (1/m)*np.dot(X, (A - y).T)
    db = (1/m)*np.sum(A - y)

    assert(dw.shape = w.shape)
    assert(db.dtype = float)

    gradient = {'dw': dw,
                'db': db}

    return gradient, cost

def optimize(w, b, X, y, iterations, learning_rate):
    '''
    w: weights, [n 1]
    b: scaler
    X: a matrix, [n m]
    y: a vector, [m 1]
    iterations: int
    learning_rate: float
    return
    '''
    costs = []

    for i in iterations:
        gradient, cost = propagate(w, b, X, y)
        dw = gradient['dw']
        db = gradient['db']

        w = w - learning_rate*dw
        b = b - learning_rate*db

        costs.append(cost)

    parameters = {'w':w,
                  'b':b}

    return parameters

def prediction(w, b, X):

    m = X.shape[0]
    y_pred = np.zeros((1, m))
    z = np.dot(w.T, X) + b
    A = sigmod(z)

    for i in range(m):
        y_pred[0, i] = 1 if A[0, i] > 0.5 else 0

    return y_pred

def model(X_train, y_train, X_test, y_test, iterations, learning_rate):
    n = X_train.shape[0]
    w, b = initialize(n)

    parameters = optimize(w, b, X_train, y_train, iterations, learning_rate)

    w, b = parameters['w'], paramters['b']
    y_pred = prediction(w, b, X_test)

    return y_pred
