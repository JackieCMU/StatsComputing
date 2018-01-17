def findShortestSubArray(nums):
    count = {}
    for v, p in enumerate(nums):
        if v not in count:
            count[v] = [p]
        else:
            count[v].append(p)
    degree, length = max([len(l) for l in count.values()]), 2**32-1
    for v in count:
        if len(count[v]) == degree:
            length = min(length, count[v][-1] - count[v][0] + 1)
    return length
