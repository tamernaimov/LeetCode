def missingNumber(nums):
    unique_list = []
    for i in range(len(nums)):
        unique_list.append(nums[i])


    for i in range(len(nums)):
        if i not in unique_list:
            print(i)
            return i
    return len(nums)

print(missingNumber([2,1,0,3]))