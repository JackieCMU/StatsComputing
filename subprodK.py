def f(nums, k):
    if k <= 1:
        return 0
    prod = 1
    left, ans = 0, 0
    for right, v in enumerate(nums):
        prod *= v
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
