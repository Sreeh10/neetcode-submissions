class Solution:
    def getSum(self, a: int, b: int) -> int:
        

        # 000100 --> 4
        # 111111 --> -1
        # 111110 --> -2
        # 111101 --> -3
        # 111100 --> -4
        # 111011 --> -5

        # 111111  = ans

        # 000100 --> 4
        # 111100 --> -4
        # 000000

        # 000100 --> 4
        # 111101 --> -3
        # 000001 --> 1

        # 000100 --> 4
        # 111011 --> -5

        # 111111 --> -1 (2^32)
        # 111110 --> 2
        # 000000 -->
        # 111111
        # 000001
        # 111110

        # last carry = 1 => -ve 
        # last carry = 0 => +ve 

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
            # print(sum_bit)
            return rolling
        else:
            # print(rolling)
            return ((~0) ^ (x)) | rolling

        # 111111111111
        # 111111111111

        # 111111110100
        # 111111111000
        # 111111101100 # 2^32 - 20
        # 100000000000
        # 011111110011        
        # 000000010011 # 19

        # 111111111111
        # 111111101100
        # 
        # 000000010011 # ~rolling
        # 111111111111
        # 111111101100     
        # if last carry = 0
