def a_in_b (a:dict, b:dict) -> bool:
    for k,v in a.items():
        if b.get(k,0) < v:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # a bit special:
        # move left pointer to nudge 
        # move right pointer to stabilize
        # system starts with an unstable state

        l = 0
        r = 0
        t_freq = {}

        for t_c in t:
            t_freq[t_c] = t_freq.get(t_c,0) + 1
        
        
        # under_freq_count stands for no of unique characters whose freq in window is less than their freq t
        under_freq_count = len(t_freq.keys()) # count unique in t
        ans = ""
        win = {}
        win[s[r]] = 1
        if win[s[r]] == t_freq.get(s[r],0):
            under_freq_count -= 1

        while l <= r:
            # print(s[l:r+1], f"{l=} {r=} {ans=} ufc={under_freq_count}", a_in_b(a=t_freq , b=win), t_freq, win)
            # if not a_in_b(a=t_freq , b=win):  # ----- unstable -> stabilize ----------
            if under_freq_count > 0:  # ----- unstable -> stabilize ----------
                r += 1
                if r >= len(s):
                    return ans # t doesnt fit in s[l:-1], hence no other sub window
                win[s[r]] = win.get(s[r],0) + 1
                if win[s[r]] == t_freq.get(s[r],0): # it became equal when raised by 1, means was under_freq and now match_freq
                    under_freq_count -= 1
                
            else: # ------- stable -> record or explore ---------
                if ans == "" or r + 1 - l < len(ans):
                    ans = s[l:r+1] 
                else: # just dont explore right when you got the answer, explore from the next iteration
                    win[s[l]] -= 1
                    if win[s[l]] < t_freq.get(s[l],0):
                        under_freq_count += 1
                    l += 1
        
        return ans
