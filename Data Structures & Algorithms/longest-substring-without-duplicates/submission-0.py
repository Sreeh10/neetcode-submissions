class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0
        curr = 1
        maxx = 1
        active = {s[l] : 1}

        # explore-stabilize motion
        # right pointer explores 1 tile
        # left pointer moves until stabilizes
        while r < len(s)-1:
            r += 1
            active[s[r]] = active.get(s[r],0) + 1
            while active.get(s[r],0) > 1:
                active[s[l]] -= 1
                l += 1
            curr = r + 1 - l
            maxx = max(maxx, curr)
            

        return maxx
