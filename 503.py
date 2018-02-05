def nextGreaterElements(nums):
    d = {}
    ans = []
    stack = []
    nums_ = nums*2

    for num in nums_:
        while len(stack) and stack[-1] < num:
            put = stack.pop()
            if put not in d:
                d[put] = [num]
            else:
                d[put].append(num)
        stack.append(num)

    for num in nums:
        ans.append(d[num].pop(0) if num in d else -1)

    return ans
