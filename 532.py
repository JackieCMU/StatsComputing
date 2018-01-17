def findParis(nums, k):
    count = 0
    d = collections.Counter(nums)
    for n in d:
        if k > 0 and n + k in d or k == 0 and d[n] > 1:
            count += 1
    return count
