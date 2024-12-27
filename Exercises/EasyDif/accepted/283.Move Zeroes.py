def moveZeroes(nums):
    counter = 0
    anotherList = []
    for i in range(len(nums)):
        if nums[i] == 0:
            counter += 1

    for i in range(len(nums)):
        if nums[i] != 0:
            anotherList.append(nums[i])
    for i in range(counter):
        anotherList.append(0)
    nums[:] = anotherList
    return nums


def moveZeroess(nums):
    l = 0
    r = 0
    while l< len(nums):
        if nums[l] == 0:
            nums[l], nums[r] = nums[r], nums[l]
            r+=1
        l+=1
    return nums


print(moveZeroess([0,1,0,3,12]))