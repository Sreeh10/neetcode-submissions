class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] = 1 + min (dp[i-c1], dp[i-c2], dp[i-c3] ....)

        dp = [0 for i in range(amount+1)]
        for c in coins:
            if c > amount:
                break
            dp[c] = 1

        consider = []
        for i in range(1,amount+1):
            if dp[i] == 1:
                consider.append(i)
            else:
                ext = []
                for c in consider:
                    if dp[i-c] > 0 :
                       ext.append(dp[i-c])
                if len(ext) > 0:
                    dp[i] = 1 + min(ext)
            
        # print(dp)
        return dp[amount] if dp[amount] > 0 or amount == 0 else -1

        