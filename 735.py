def asteroidCollision(asteroids):
    res = []
    for a in asteroids:
        while res and a < 0 < res[-1]:
            if res[-1] < -a:
                res.pop()
                continue
            elif res[-1] == -a:
                res.pop()
            break
        else:
            res.append(a)
    return res
