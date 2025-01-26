def numberOfSubarrays(nums, k):
    def atMostK(k):
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0: 
                k -= 1
            while k < 0:
                if nums[left] % 2 != 0:
                    k += 1
                left += 1
            count += right - left + 1
        return count

    return atMostK(k) - atMostK(k - 1)


print(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
