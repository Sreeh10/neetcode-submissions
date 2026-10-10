class Solution:
    def countSubstrings(self, s: str) -> int:
        ans : int = 0
        # introduce . between each pair of characters to make it odd only palindromic
        s = ".".join([x for x in s])

        # print(f"{len(s)=}")
        for i in range(len(s)):
            ans += (0 if s[i] == "." else 1) # 1 length substrings are considered palindrome
            left = i- (1 if s[i] == "." else 2)
            right = i+ (1 if s[i] == "." else 2)
            # print(f"@{i=} {left=} {right=} {ans=}")
            while left >= 0 and right < len(s):
                # print(s[left:right+1], ans)
                if s[left] == s[right]:
                    # print(f"\t{s[left:right+1]}")
                    ans += 1
                else:
                    break
                left -= 2 # skip the dot and jump to next char
                right += 2 # skip the dot and jump to next char

        return ans
        