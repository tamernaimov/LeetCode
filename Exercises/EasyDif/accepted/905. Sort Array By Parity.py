def sortArrayByParity(nums):
    even = []
    odd = []

    for i in range(len(nums)):
        if nums[i] % 2 ==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    res = []
    for i in range (len(even)):
        res.append(even[i])
    for i in range (len(odd)):
        res.append(odd[i])

    return res

print(sortArrayByParity([3,1,2,4]))
