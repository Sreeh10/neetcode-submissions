class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum_bit = 0
        carry_bit = 0
        pos = 1
        rolling = 0
        x = 0
        for i in range(32):
            a_bit = a%2 
            b_bit = b%2
            sum_bit = a_bit ^ b_bit ^ carry_bit
            carry_bit = (carry_bit & a_bit) | (a_bit & b_bit) | (b_bit & carry_bit)
            a >>= 1
            b >>= 1
            rolling = (sum_bit << i) | rolling
            x <<= 1
            x |= 1

        if not carry_bit:
            if not sum_bit:
                return rolling
            else:
                return ((~0) ^ (x)) | rolling
        if not sum_bit :
            return rolling
        else:
            return ((~0) ^ (x)) | rolling