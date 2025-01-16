def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            sumUp = nums[i] + nums[l] + nums[r]

            if sumUp > 0:
                r -= 1
            elif sumUp < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return res
print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
