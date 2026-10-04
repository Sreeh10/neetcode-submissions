class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freq = {s[r] : 1}
        # explore stablize
        
        window_max_freq = 0
        max_window_len = 0

        while r < len(s):
            window_max_freq = max(window_max_freq, freq.get(s[r],0))
            window_len = r + 1 - l
            if window_max_freq + k >= window_len: # valid window or we already had a valid window larger than this -> explore 
                max_window_len = max(max_window_len, window_len)
                # print(s[l:r+1], f"{l=}, {r=}, {window_max_freq=}, {window_len=}, {max_window_len=}, {k=}", " valid or <= than found")
                r += 1
                if r >= len(s):
                    break
                freq[s[r]] = freq.get(s[r],0) + 1
            else: # invalid window -> stablize
                # print(s[l:r+1], f"{l=}, {r=}, {window_max_freq=}, {window_len=}, {k=}", " -- invalid")
                freq[s[l]] -= 1
                l += 1

        # return min(len(s),window_max_freq + k)
        return max_window_len
            
