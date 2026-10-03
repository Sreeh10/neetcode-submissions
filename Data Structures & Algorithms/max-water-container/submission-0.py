class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # anything that can store more water than current L<->R
        # always requires to move the smaller of L or R inwards
        # if both are equal, then any greater solution will always be strictly inside current L<->R, requiring both move inward

        l = 0
        r = len(heights)-1
        maxx = 0
        while (l <= r):
            curr = (r-l) * min(heights[l],heights[r])
            maxx = max(maxx, curr)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-= 1
        
        return maxx
        

        
            

        