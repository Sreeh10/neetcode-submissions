class Solution:
    def longestPalindrome(self, s: str) -> str:

        s = ".".join([x for x in s])

        if len(s) == 0:
            return 0
        
        ans:str = s[0]

        for i in range(len(s)):
            left = i-(1 if s[i] == "." else 2)
            right = i+(1 if s[i] == "." else 2)
            # print(f"@{i=}")
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    # print(f"\t{left=} {right=} {ans=}")
                    if len(ans) < ((right + 2 - left)//2): # works for both odd length and even length strings
                        ans = s[left:right+1:2] # left and right are never on dots
                else:
                    break
                left -= 2
                right += 2

        
        return ans