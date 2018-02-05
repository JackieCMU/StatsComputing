def lengthOfLongestSubstring(s):
    length = start = 0
    existed = {}
    for p, v in enumerate(s):
        if v in existed and start <= existed[v]:
            start += existed[v] + 1
        else:
            length = max(length, p - start + 1)
        existed[v] = p
    return length
