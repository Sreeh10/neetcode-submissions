class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
        
        # for x in dp:
        #     print(x)
        return dp[-1][-1]