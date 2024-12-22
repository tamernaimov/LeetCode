def findDuplicate(nums):
    unique_list = []
    for i in range (len(nums)):
        if nums[i] not in unique_list:
            unique_list.append(nums[i])
        else:
            return nums[i]



print(findDuplicate([1,3,4,2,2]))