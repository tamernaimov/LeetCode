def majorityElement(self,nums):
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 0

        for i in range(len(nums)):
            hm[nums[i]] += 1
        for item in hm:
            if hm.get(item) > len(nums)/2:
                return item
