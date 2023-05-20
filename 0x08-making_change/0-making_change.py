#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """Adding two arrays"""
    if total <= 0:
        return 0

    # verify coins is a valid
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    my_coins = sorted(coins, reverse=True)
    money_left = total

    for coin in my_coins:
        while (money_left % coin >= 0 and money_left >= coin):
            change += int(money_left / coin)
            money_left = money_left % coin

    change = change if money_left == 0 else -1

    return change


print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
