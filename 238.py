def productExceptSelf(nums):
    prod = 1
    output = []
    for n in nums:
        output.append(prod)
        prod *= n
    prod = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= prod
        prod *= nums[i]
    return output
