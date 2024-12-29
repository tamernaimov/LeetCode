def findMaxAverage(nums, k):
        current_sum = sum(nums[:k])
        maximum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # slide the window
            maximum = max(maximum, current_sum)

        return maximum / k