def nextGreaterElement(findNums, nums):
    d = {}
    stack = []
    ans = []
    for num in nums:
        while len(stack) and stack[-1] < num:
            d[stack.pop()] = num
        stack.append(num)

    for num in findNums:
        ans.append(d.get(num, -1))

    return ans
    
