from itertools import permutations
def getPermutation(n,k):
    nums = []
    for i in range (1,n+1):
        nums.append(str(i))



    nums = permutations(nums)
    nums = [list(perm) for perm in nums]



    return ''.join(nums[k-1])

print(getPermutation(3,3))