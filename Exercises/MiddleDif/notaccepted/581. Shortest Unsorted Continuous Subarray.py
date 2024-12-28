

def findUnsortedSubarray(nums):
    if len(nums) == 1:
        return nums[0]

    nums2 =nums[::1]
    nums.sort()
    sortedNums = nums[::1]

    if nums2 == sortedNums:
        return 0


    longest = 0

    for i in range(len(nums)):
        counter = 0
        l = i
        r = len(nums)
        while l < r:
            sn = nums2[l:r]
            print(sn)
            if sn == sortedNums:
                counter = len(sn)
                l += 1
                continue
            l+=1
        if counter > longest:
            longest = counter

    return longest


print(findUnsortedSubarray([2,6,4,8,10,9,15]))