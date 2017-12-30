def f(prices):

    maxsofar = 0
    maxcur = 0
    if len(prices) <= 1:
        return maxsofar
    else:
        for i in range(1, len(prices)):
            maxcur += prices[i] - prices[i-1]
            maxcur = max(0, maxcur)
            maxsofar = max(maxsofar, maxcur)
    return maxsofar
