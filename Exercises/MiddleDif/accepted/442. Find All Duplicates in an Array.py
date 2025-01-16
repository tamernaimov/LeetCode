def findDuplicates(nums):

    seen = set()
    res = []
    for i in range (len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            res.append(nums[i])

    return res

print(findDuplicates([4,3,2,7,8,2,3,1]))