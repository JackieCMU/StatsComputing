def repeatedStringMatch(A, B):
    n = len(B)//len(A) + 1 if len(B) % len(A) != 0 else len(B)//len(A)
    for i in range(2):
        if B in A*(n+i):
            return n+i
    return -1
