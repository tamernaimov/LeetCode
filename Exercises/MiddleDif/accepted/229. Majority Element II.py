def majorityElement(nums):
        hm = {}
        unique_list = []
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 0

        for i in range(len(nums)):
            hm[nums[i]] += 1
        for item in hm:
            if hm.get(item) > len(nums)/3:
                unique_list.append(item)

        return unique_list

print(majorityElement([3,3,1]))