def triangleNumber(nums):
    nums.sort()
    count = 0
    if len(nums) <= 2:
        return count
    for i in range(0, len(nums)-2):
        k = i + 2
        if nums[i] != 0:
            for j in range(i + 1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
    return count
