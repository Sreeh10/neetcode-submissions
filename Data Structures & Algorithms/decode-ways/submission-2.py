class Solution:
    def numDecodings(self, s: str) -> int:

        # dp[i] # no of decodings considering only upto s[i]

        allowed = [str(x) for x in range(1,26+1)]
        dp = [0 for i in range(len(s))]
        dp[0] = 1 if s[0] in allowed else 0
        if len(s) == 1:
            return dp[0]

        dp[1] = (
                    (dp[0] * (1 if s[1:1+1] in allowed else 0))
                    + (1 if s[0:1+1] in allowed else 0)
                )

        for i in range(2, len(s)):
            dp[i] = (
                        dp[i-1] * (1 if s[i:i+1] in allowed else 0)
                        + dp[i-2] * (1 if s[i-1:i+1] in allowed else 0)
                    )
        # print(dp)
        return dp[len(s)-1]