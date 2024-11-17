

def singleNumber(nums): # do that with a hashmap
    my_list_dict = {}
    for i in range(len(nums)):
        if nums[i] not in my_list_dict:
            my_list_dict[nums[i]] = 0

    for i in range(len(nums)):
        if nums[i] in my_list_dict:
            my_list_dict[nums[i]] +=1

    for i in range(len(nums)):
        if my_list_dict[nums[i]] == 1:
            return nums[i]

    print(my_list_dict)


print(singleNumber([1,1,2,2,3,3,4,5,5,6,6]))
