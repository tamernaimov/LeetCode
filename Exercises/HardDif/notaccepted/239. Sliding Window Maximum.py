from collections import deque
def maxSlidingWindow(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    dq = deque()
    result = []

    for i in range(n):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)


        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(maxSlidingWindow([3,1,-1,-3,5,3,6,7],3)) #[3,1,5,5,6,7]