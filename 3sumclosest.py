def f1(nums, target):
    nums.sort()
    res = 0
    dis = 2**32-1
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            l = [nums[i], nums[j], nums[k]]
            if sum(l) == target:
                return target
            if abs(sum(l) - target) < dis:
                dis = abs(sum(l) - target)
                res = sum(l)
            elif sum(l) > target:
                k -= 1
            else:
                j += 1
    return res
