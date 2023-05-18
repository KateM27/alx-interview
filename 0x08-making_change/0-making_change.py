#!/usr/bin/python3
def makeChange(coins, total):
    # If the total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of
    # coins needed for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each
        # value from the current coin to the total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the minimum number of coins for the total is still
    # infinity, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]


print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
