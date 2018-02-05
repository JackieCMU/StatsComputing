def optimalDivision(nums):
    nums = map(str, nums)
    res = ''
    if len(nums) <= 2:
        return '/'.join(nums)
    return '{}/({})'.format(nums[0], '/'.join(nums[1:]))
