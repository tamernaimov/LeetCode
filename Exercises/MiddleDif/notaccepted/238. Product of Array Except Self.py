

def productExceptSelf(nums): #this should work idk why it doesnt tho like the fuck
    unique_list = []
    cur_nums = nums
    for i in range(len(nums)):
        unique_list = cur_nums[:]
        print(unique_list)
        nums[i] = 1
        for j in range(len(unique_list)):
            nums[i] *= unique_list[j]

    return nums

print(productExceptSelf([1,2,3,4]))