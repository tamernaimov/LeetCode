def longestConsecutive(nums):
    if not nums:
        return 0
    nums.sort()
    nums = list(dict.fromkeys(nums))
    longestCounter = 0
    counter = 0
    print(nums)
    for i in range(len(nums)-1):

        if nums[i] == nums[i+1]-1 or nums[i] == nums[i+1]:
            if nums[i] == nums[i+1]:
                continue
            else:
                counter +=1
        else:
            counter = 0
        if counter > longestCounter:
            longestCounter = counter

    return longestCounter + 1

print(longestConsecutive([0,-1]))