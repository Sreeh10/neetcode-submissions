class Solution:
    def isPalindrome(self, s: str) -> bool:
        # implement -> alphanumeric(s)
        new_s = ""
        for s_c in s :
            if s_c.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                new_s += s_c.upper()
        # print(new_s)
        s = new_s
        l = 0
        r = len(s) - 1
        while (l<=r):
            if s[l] != s[r]:
                # print(l, r, s[l], s[r])
                return False
            l += 1
            r -= 1
        return True
        