def f1(nums):
    nums.sort()
    res = []
    i = 0
    while i < len(nums) - 2:
        j = i+1
        k = len(nums) - 1
        while j < k:
            l = [nums[i], nums[j], nums[k]]
            if sum(l) == 0:
                res.append(l)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j +=1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif sum(l) < 0:
                j +=1
            else:
                k -= 1
        i += 1
        while i < len(nums) - 2 and nums[i] == nums[i-1]:
            i += 1
    return res

def f2(nums):
    res = set()
    nums.sort()
    if len(nums) < 3:
        return []
    for i, v in enumerate(nums[:-2]):
        if i >=1 and v == nums[i-1]:
            continue
        d = {}
        for num in nums[i+1:]:
            if num not in d:
                d[-v-num] = 1
            else:
                res.add((v, num, -v-num))
    return map(list, res)
