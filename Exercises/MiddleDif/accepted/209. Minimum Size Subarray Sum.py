def minSubArrayLen(target, nums):
        l = 0
        r = 0
        current_sum = nums[0]
        minimum_length = len(nums)
        n = 1
        checker = False

        while r < len(nums):
            if current_sum < target:
                r+=1
                if r < len(nums):
                    current_sum += nums[r]
                    n+=1
            else:
                checker = True
                while current_sum >= target:
                    minimum_length = min(minimum_length, n)
                    current_sum -= nums[l]
                    l += 1
                    n -= 1

        if not checker:
            return 0

        return minimum_length


print(minSubArrayLen(7,[2,3,1,2,4,3]))