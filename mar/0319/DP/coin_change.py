# Coin Change
# Pattern: DP (Min Coins, Unlimited Use)
# Difficulty: Medium

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(amount + 1):
            if coin <= j:
                dp[j] = min(dp[j], 1 + dp[j - coin])
    return dp[amount]
