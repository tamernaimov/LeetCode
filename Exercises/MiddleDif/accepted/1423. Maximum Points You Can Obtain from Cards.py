def maxScore(cardPoints, k):
    n = len(cardPoints)
    window = cardPoints[:n - k]
    lowest = sum(window)
    curSum = lowest

    for i in range(n - k, n):
        curSum += cardPoints[i]
        curSum -= cardPoints[i - (n - k)]

        if curSum < lowest:
            lowest = curSum

    return sum(cardPoints) - lowest



print(maxScore([6,1,2,4,6,8,2,4,4,1,2,3,5,6,1,2,4,5,6,1,32,46],6))