def containsNearbyAlmostDuplicate(nums,indexDiff,valueDiff):

    for i in range (len(nums)):
        if (i+ indexDiff) < len(nums):
            for j in range(i+indexDiff,len(nums)):
               if abs(i-j) <= indexDiff:
                   if abs(nums[i] - nums[j]) <= valueDiff:
                       return True


    return False

print(containsNearbyAlmostDuplicate([1,2,3,1],3,0))