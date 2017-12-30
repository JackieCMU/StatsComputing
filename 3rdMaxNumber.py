def f(nums):
    f, s, t = -2**32, -2**32, -2**32
    for num in nums:
        if num not in [f,s,t]:
            if num > f:
                f, s, t = num, f, s
            elif num > s:
                s, t = num, s
            elif num > t:
                t = num
    if t != -2**32:
        return t
    else:
        return f
