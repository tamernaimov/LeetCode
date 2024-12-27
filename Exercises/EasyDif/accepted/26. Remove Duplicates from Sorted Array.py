def removeDuplicates(nums):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)-1):
            if nums[i] == nums[j]:
                nums.pop(j)

    return nums

print(removeDuplicates([1,1,2]))