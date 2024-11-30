def maxProfit(prices):
    lowest = 2147483647
    lowestIndex = 0
    for i in range(len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
    lowestIndex = prices.index(lowest)
    biggest = -2147483647
    check1 = False
    for i in range(lowestIndex+1, len(prices)):
        if prices[i] > biggest:
            biggest = prices[i]
            check1 = True

    if not check1:
        return 0

    return biggest - lowest



print(maxProfit([-1,6,1,2,3,4]))