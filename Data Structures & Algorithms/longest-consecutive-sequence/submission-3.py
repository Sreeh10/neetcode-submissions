def explore_chain(x,s):
    count = 0
    while x in s:
        # print(x, end="")
        x += 1
        count += 1
    # print("")
    return count
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1st pass - put everything in a hash table
        # start at the in elem of array and explore chain of presence and note the window to not touch again
        # then examine chain of presence with every elem of the array aand keep updating the window
        if len(nums) == 0:
            return 0
        s = set(nums)
        mn = min(nums)
        max_chain_len = 0
        chain_end = mn
        for n in [mn]+nums:
            if (n-1 not in s): # in order to start only from possible chain heads
                chain_len = explore_chain(n,s)
                max_chain_len = max(max_chain_len, chain_len)
        
        return max_chain_len



        