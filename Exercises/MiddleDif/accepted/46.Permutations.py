import itertools
def permute(nums):
    permutations = itertools.permutations(nums)
    unique_numbers = {''.join(map(str, p)) for p in permutations}
    unique_integers = [int(num) for num in unique_numbers]
    nums = list(set(unique_integers))
    print(nums)

    unique_list = []
    for i in range(len(nums)):
        unique_list2 = []
        strNum = str(nums[i])
        for x in range(len(strNum)):
            temp = int(strNum[x])
            unique_list2.append(temp)

        for j in range(len(str(nums[i]))):
            unique_list.append(unique_list2)

    unique_list = [list(t) for t in set(tuple(lst) for lst in unique_list)]

    return unique_list
print(permute([0,1]))