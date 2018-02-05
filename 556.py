def nextGreaterElement(n):
    right, minright, find = 0, {}, False
    s = list(str(n))
    for i in range(len(s)-1, 0, -1):
        if int(s[i]) > int(s[i-1]):
            right = i - 1
            find = True
            break
    if not find or n > 2**32:
        return -1
    else:
        for i in range(right, len(s)):
            if s[i] > s[right] and s[i] not in minright:
                minright[s[i]] = [i]
            elif s[i] > s[right]:
                minright[s[i]].append(i)
        left = minright[min(minright.keys())][-1]
        s[right], s[left] = s[left], s[right]
        s[right+1:] = s[right+1:][::-1]
    return int(''.join(s))
