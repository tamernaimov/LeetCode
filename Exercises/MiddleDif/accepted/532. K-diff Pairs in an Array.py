def findPairs(nums, k):
    if k < 0:
        return 0  # No valid pairs for negative k

    count = {}
    result = 0

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in count:
        if k == 0:
            if count[num] > 1:
                result += 1
        else:
            if num + k in count:
                result += 1

    return result

print(findPairs([1,2,4,4,3,3,0,9,2,3],3))