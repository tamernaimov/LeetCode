def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    i = 0
    max_counter = 0
    counter = 0
    print(nums)
    while i < len(nums)-1:
        if nums[i]+1 == nums[i+1]:
            counter+=1
        else:
            if counter > max_counter:
                max_counter = counter
            counter = 0
        i+=1
        if i == len(nums)-1:
            if counter > max_counter:
                max_counter = counter

    return max_counter +1


print(longestConsecutive([0,-1]))