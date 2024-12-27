def lengthOfLIS(nums): #dont get the idea
    counter = 0
    longestCounter = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            counter += 1
        else:
            counter = 0

        if counter > longestCounter:
            longestCounter = counter

    return longestCounter

print(lengthOfLIS([5,1,2,3,5,1,1,2,3,4,5,6,7]))