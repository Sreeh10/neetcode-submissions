class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_index_reachable = nums[0]

        for i in range(1, len(nums)):
            if i <= max_index_reachable:
                max_index_reachable = max(max_index_reachable, i + nums[i])
        
        return (max_index_reachable >= (len(nums) - 1 )) 

        