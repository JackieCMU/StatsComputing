def removeKdigits(num, k):
    while k > 0:
        k -= 1
        i = 0
        while i < len(num) - 1:
            if num[i] > num[i+1]:
                break
            i += 1
        num = num[:i] + num[i+1:]
    if len(num) == 0:
        return '0'
    return str(int(num))
