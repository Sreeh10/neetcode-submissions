class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp[i][j] -> consider upto index i in first string, index j in second string
        if len(text1) == 0 or len(text2) == 0:
            return 0

        dp = [[0 for t_j in text2] for t_i in text1]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        # fill i ==0
        for j in range(1,len(text2)):
            dp[0][j] = 1 if (dp[0][j-1] == 1) or (text1[0] == text2[j]) else 0
        # fill j ==0 
        for i in range(1,len(text1)):
            dp[i][0] = 1 if (dp[i-1][0] == 1) or (text1[i] == text2[0]) else 0
        
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # for x in dp:
        #     print(x)

        return dp[-1][-1]