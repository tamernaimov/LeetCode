def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    for i in range (len(nums)):
        if i == 0:
            if nums[i] > nums[i+1]:
                return i
        if i == len(nums)-1:
            if nums[i] > nums[i-1]:
                return i
        if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
            return i

print(findPeakElement([1]))