def lengthOfLIS(nums):
    counter = 0
    longestCounter = 0
    nums = list(dict.fromkeys(nums))
    print(nums)
    for i in range (len(nums)):
        temp = nums[i]
        counter = 0
        for j in range (i+1,len(nums)):
            if temp < nums[j]:

                counter+=1
                temp = nums[j]
        if counter > longestCounter:
            longestCounter = counter
    return longestCounter+1

print(lengthOfLIS([0,1,0,3,2,3])) #logic not working