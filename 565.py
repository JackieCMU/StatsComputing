def arrayNesting(nums):
    res = 0
    visited = set()
    for i in range(len(nums)):
        count = 1
        start = nums[i]
        if i not in visited:
            visited.add(i)
            while start != i:
                visited.add(start)
                count += 1
                start = nums[start]
            res = max(res, count)
    return res
