class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)-1): #1
            n = i+1 #2
            for n in range(i+1, len(nums)):
                if nums[i] + nums[n] == target: #1 + #2
                    return i,n