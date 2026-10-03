class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0
        curr = 1
        maxx = 1
        active = set(s[l])
        # explore-stabilize motion
        # right pointer explores 1 tile
        # left pointer moves until stabilizes
        while r < len(s)-1:
            r += 1
            while s[r] in active: # there will atmost be only 1 occurance of each character in the current window anyway
                active.remove(s[l])
                l += 1
            active.add(s[r])
            curr = r + 1 - l
            maxx = max(maxx, curr)
            

        return maxx
