class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # dp[i] = no of set bits in number i 

        # dp[i] = 1 + dp[i-nearest power of 2 ]

        dp = [0, 1, 1]
        nearest_pow_of_2 = 2
        for i in range(3, n+1):
            if i == 2 * nearest_pow_of_2 :
                nearest_pow_of_2 *= 2
                dp.append(1)
            else:
                dp.append(1 + dp[i-nearest_pow_of_2])
        
        return dp[:n+1]

        #    0
        #    1  -- 0 - 1
        #   10  -- 1 - 1
        #   11 
        #  100 -- 2 - 3
        #  101 
        #  110
        #  111
        # 1000 -- 3 - 8
        # 1001
        # 1010
        # 1011
        # 1100
        # 1101
        # 1110
        # 1111
    #    10000 -- 4 - 20


        