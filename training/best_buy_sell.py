prices = [7, 1, 5, 3, 6, 4]

left = 0      # Buy pointer
right = 1     # Sell pointer
max_profit = 0

while right < len(prices):

    # If selling gives profit
    if prices[left] < prices[right]:
        current_profit = prices[right] - prices[left]

        if current_profit > max_profit:
            max_profit = current_profit

    # Found a lower buying price
    else:
        left = right

    right += 1

print("Maximum Profit =", max_profit)