def findUnsortedSubarray(nums):
    n = len(nums)
    
    left, right = -1, -1
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                if left == -1:
                    left = j
                right = j + 1
    
    if left == -1:
        return 0
    else:
        return right - left + 1

nums = [2,4,6,8,10,9,15,10,5]
print(findUnsortedSubarray(nums))  # Output: 5