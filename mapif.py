from functools import reduce

def mapif(s, pred = lambda x : True, f = lambda x : x):
    '''
    s: a list
    pred: function
    f: function
    return: a list
    '''
    def helper(container, x):
        if pred(x):
            container.append(f(x))
            return container
        else:
            container.append(x)
            return container
    return reduce(helper, s, [])

def partition(s, size, step = None):
    '''
    s: a list
    size: a number
    step: a number
    return: a list
    '''
    step = size if step is None else step
    startIndex = mapif(range(len(s)), lambda x : x % step != 0, lambda x : None) # find the start index of each step
    def helper(container, x):   # a helper function to put the required list in result
        skip, result = container
        if type(x) == int:
            result.append(s[x:(size+x)])
            return [skip, result]
        else:
            return [skip, result]
    return reduce(helper, startIndex, [[], []])[1]
