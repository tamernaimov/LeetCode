def maxProfit(prices):
    biggestProfit = 0
    bp = prices[0]

    for i in range (len(prices)):
        if prices[i]< bp:
            bp = prices[i]
        if prices[i] - bp > biggestProfit:
            biggestProfit = prices[i] - bp

    return biggestProfit


print(maxProfit([1,2,0,3]))