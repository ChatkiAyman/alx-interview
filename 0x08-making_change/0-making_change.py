#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): The values of the coins available.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total < 0:
        return -1
    if total == 0:
        return 0
    if not coins:
        return -1

    # Initialize DP table with a value larger than the maximum possible coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
