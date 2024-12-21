def maxProfit(prices):
    biggestProfit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > biggestProfit:
                biggestProfit = prices[j]-prices[i]
    return biggestProfit



print(maxProfit([1,2]))