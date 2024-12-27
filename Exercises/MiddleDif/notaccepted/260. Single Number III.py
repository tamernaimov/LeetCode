def singleNumber(nums):
    nums1 = []
    counter = 0
    for i in range(len(nums)):
        if nums[i] in nums:
            counter+=1

        if counter == 1:
            nums1.append(nums[i])

    return nums1

print(singleNumber([5,4,1,1,5]))