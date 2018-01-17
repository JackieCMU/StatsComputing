def judgeCircle(moves):
    L = R = U = D = 0
    for m in moves:
        if m == 'L':
            L += 1
        elif m == 'R':
            R += 1
        elif m == 'U':
            U += 1
        else:
            D += 1
    if L == R and U == D:
        return True
    else:
        return False
