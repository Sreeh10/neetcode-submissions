class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # dp[i] : bool -> whether string considering only upto i can be broken into dictionary words
        dp = [False for i in range(len(s))]
        dp[0] = True if s[0:1] in wordDict else False
        wordLens = set([len(w) for w in wordDict])

        for w_len in wordLens:
            if s[0:w_len] in wordDict:
                dp[w_len-1] = True

        for i in range(1,len(s)):
            for w_len in wordLens:
                if (i+1) >= w_len:
                    if dp[i-w_len]:
                        if s[i+1-w_len : i+1] in wordDict:
                            dp[i] = True

        print(wordLens)
        print(dp)
        return dp[len(s)-1]

        