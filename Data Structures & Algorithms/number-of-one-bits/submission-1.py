class Solution:
    def hammingWeight(self, n: int) -> int:
        # ans = 0
        # while n > 0 :
        #     ans += n%2
        #     n //= 2
        # return ans

        ans = 0
        while n > 0:
            n = n & (n-1)
            ans += 1

        return ans        