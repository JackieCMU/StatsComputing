def f(prices, fee):
    sold = [0]*len(prices)
    hold = [0]*len(prices)
    hold[0] = -prices[0]

    for i in range(1, len(prices)):
        sold[i] = max(sold[i-1], hold[i-1] + prices[i] - fee)
        hold[i] = max(hold[i-1], sold[i-1] - prices[i])
    return max(max(sold), max(hold))
