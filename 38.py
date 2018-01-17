def countAndSay(n):
    res = '1'
    for _ in range(n-1):
        l, r, count = res[0], '', 0
        for n in res:
            if l == n:
                count += 1
            else:
                r += str(count) + l
                l = n
                count = 1
        r += str(count) + l
        res = r
    return res
