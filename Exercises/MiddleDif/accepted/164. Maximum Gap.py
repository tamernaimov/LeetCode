def maximumGap(nums):
    nums.sort()
    biggestDif = 0
    print(nums)
    for i in range (len(nums)-1):
        difference = nums[i+1] - nums[i]
        if difference > biggestDif:
            biggestDif = difference
    return biggestDif
print(maximumGap([3,6,9,1]))