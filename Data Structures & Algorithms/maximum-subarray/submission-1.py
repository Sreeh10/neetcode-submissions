class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each step, there are 2 decisions, include the element or exclude this
        # why will we exclude? only if it is a negative element
        # that means any subsegment will always start with a postive number
        # so at each elem, basically we are deciding whether te subsegment starts at this element or this element just adds to the prev sum

        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1] + nums[i] , nums[i]))
            
        return max(dp)
        
