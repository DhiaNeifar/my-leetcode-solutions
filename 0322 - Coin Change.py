class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if len(coins) == 1 and amount % coins[0] == 0:
            return amount // coins[0]

        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        coins = set(coins)
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != amount + 1 else -1