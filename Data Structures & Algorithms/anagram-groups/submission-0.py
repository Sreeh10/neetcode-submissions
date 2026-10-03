def myhash(s: str):
    counts = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    for s_c in s:
        counts[s_c] += 1
    return "".join([(k + str(v)) for k,v in counts.items()])

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            if (h := myhash(s)) in groups:
                groups[h].append(s)
            else:
                groups[h] = [s]
        return [val for key,val in groups.items()]
        