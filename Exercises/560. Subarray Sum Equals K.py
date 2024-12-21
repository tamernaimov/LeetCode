def subarraySum(nums,k):
    counter = 0
    for i in range(len(nums)):
        curSum = 0
        for j in range (i,len(nums)):
            curSum += nums[j]
            if curSum == k:
                counter+=1
                continue
    return counter

print(subarraySum([1,1,1],2))