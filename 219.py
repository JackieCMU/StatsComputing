def containNearbyDuplicate(nums, k):
    if len(nums) <= 1:
        return False

    count = {}
    for p, v in enumerate(nums):
        if v not in count:
            count[v] = [p]
        else:
            count[v].append(p)
    existed = [v for v in count if len(count[v]) > 1]
    for num in existed:
        for x, y in zip(count[num], count[num][1:]):
            if y - x <= k:
                return True
    return False
