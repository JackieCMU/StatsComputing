def convert(s, numRows):
    contain, n, control = [], 0, True
    if numRows == 1:
        return s
    for i in range(numRows):
        contain.append([])
    for v in s:
        if n != numRows - 1 and control:
            contain[n].append(v)
            n += 1
        elif n != 0:
            contain[n].append(v)
            n -= 1
        if n == numRows - 1:
            control = False
        elif n == 0:
            control = True
    print(contain)
    return ''.join([''.join(n) for n in contain])
