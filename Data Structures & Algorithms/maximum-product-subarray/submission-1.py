class Solution:
    def maxProduct(self, nums: List[int]) -> int:        
        # dp[i][0] = min non positive product ending in element i
        # dp[i][1] = max non negative product ending in element i
        dp = [[0 if nums[0] > 0 else nums[0], 0 if nums[0] < 0 else nums[0]]]
        global_max = nums[0]
        for i in range (1,len(nums)):
            calc1 =  nums[i] * dp[i-1][0]
            calc2 = [nums[i], nums[i] * dp[i-1][1]]
            dp.append(
                [calc1,max(calc2)] if nums[i] > 0 else [min(calc2), calc1]
            )
            global_max = max(global_max, max(dp[-1]))
        return global_max
            # if nums[i] >= 0:
            #     dp.append([
            #         nums[i] * dp[i-1][0],
            #         max(nums[i], nums[i] * dp[i-1][1])
            #     ])
            # elif nums[i] < 0:
            #     dp.append([
            #         min(nums[i], nums[i] * dp[i-1][1]),
            #         nums[i] * dp[i-1][0]
            #     ])


          