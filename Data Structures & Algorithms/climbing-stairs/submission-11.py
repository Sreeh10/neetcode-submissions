class Solution:
    def climbStairs(self, n: int) -> int:
        num = [0,1,2]
        for i in range(3, n+1) :
            num.append( num[i-1] + num [i-2] ) 
        return num[n]
        