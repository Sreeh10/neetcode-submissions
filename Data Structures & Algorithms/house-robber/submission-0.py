class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0,nums[0]]]
        for i in range(1, len(nums)):
            dp.append(
                [
                    max(dp[i-1]),
                    dp[i-1][0] + nums[i]
                ]
            )
        
        return max(dp[-1])