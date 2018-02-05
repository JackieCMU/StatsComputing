def dailyTemperatures(temperatures):
    if not temperatures: return []
    res, stack = [0]*len(temperatures), []
    if len(res) == 1: return [0]
    stack.append([temperatures[0], 0])
    for i in range(1, len(res)):
        while stack:
            pre = stack[-1][0]
            if pre < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            else:
                break
        stack.append([temperatures[i], i])
    return res
