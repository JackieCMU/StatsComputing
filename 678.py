def checkValidString(s):
    pmax = pmin = 0
    for p in s:
        pmin += 1 if p == '(' else -1
        pmax += 1 if p != ')' else -1
        if pmax < 0:
            return False
        pmin = max(pmin, 0)
    return pmin == 0
