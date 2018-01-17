def repeatedSubstringPattern(s):
    for i in range(len(s)//2 + 1):
        r = len(s) % len(s[:i+1])
        m = len(s) // len(s[:i+1])
        if i == len(s) - 1:
            return False
        elif r == 0 and s[:i+1]*m == s:
            return True
    return False
