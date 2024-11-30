from itertools import permutations

def permute(nums):
    nums = permutations(nums)
    nums = [list(perm) for perm in nums]
    unique_list = []

    for i in range(len(nums)):
        if nums[i] not in unique_list:
            unique_list.append(nums[i])
    return unique_list

print(permute([1,1,2]))