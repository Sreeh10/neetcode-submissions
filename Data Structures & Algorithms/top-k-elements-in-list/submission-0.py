import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        heapq.heapify_max((g:=[(v,k) for k,v in d.items()]))
        return [a[1] for a in heapq.nlargest(k,g)]


        