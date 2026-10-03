class Solution:


    def encode(self, strs: List[str]) -> str:
        #include a header with lens of each string
        header = [len(s) for s in strs]
        return str(header)+"".join(strs)

    def decode(self, s: str) -> List[str]:
        #find first ] and split on commas to get lengths of each segment
        #edge acse - empty string
        ind = s.index(']')
        if ind==1: #empty string encoded
            return []

        lens = [int(l) for l in s[1:ind].split(",")]
        start = ind + 1
        ans = []
        for length in lens:
            ans.append(s[start: start+ length])
            start += length 

        return ans


