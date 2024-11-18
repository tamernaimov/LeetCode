def moveZeroes(nums):
    counter = 0
    anotherList = []
    for i in range(len(nums)):
        if nums[i] == 0:
            counter += 1

    for i in range(len(nums)):
        if nums[i] != 0:
            anotherList.append(nums[i])
    anotherList.sort()

    for i in range(counter):
        anotherList.append(0)
    nums[:] = anotherList  # This modifies the original `nums` list in-place
    return nums
print(moveZeroes([2,1]))