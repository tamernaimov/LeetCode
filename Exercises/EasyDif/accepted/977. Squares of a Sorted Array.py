def sortedSquares(nums):
    for i in range (len(nums)):
        nums[i] = nums[i]*nums[i]

    nums.sort()
    return nums


print(sortedSquares([4,1,2,3,1]))