def calPoints(ops):
    res = []
    for n in ops:
        if n.strip('-').isdigit():
            res.append(int(n))
        elif n == '+':
            res.append(res[-1] + res[-2])
        elif n == 'D':
            res.append(2*int(res[-1]))
        elif n == 'C':
            res.pop()
    return sum(map(int, res))
