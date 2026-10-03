class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_xor = 0
        for i in range(1,len(nums)+1):
            all_xor ^= i
        
        arr_xor = nums[0]
        for n in nums[1:]:
            arr_xor ^= n
        
        return all_xor^arr_xor
