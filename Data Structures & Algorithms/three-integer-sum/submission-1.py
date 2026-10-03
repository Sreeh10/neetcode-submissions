def find_higher_non(space:List, non:List):
    ans = []
    for i in range(len(space)):
        if space[i] not in non and space[i]> max(non):
            ans.extend(space[i:]) # take all indices after this anyway
    return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        d = {}
        for i in range(len(nums)):
            d.setdefault(nums[i], []).append(i)

        output = set()
        # for each pair, check if negative of their sum exists in the array, without repeating element
        for i in range(len(nums)):
            p = nums[i]
            for j in range(i+1, len(nums)):
                q = nums[j]
                r = - (p + q)
                # required frequency
                req_freq = 1
                req_freq += 1 if p == r else 0
                req_freq += 1 if q == r else 0

                if len(d.get(r, [])) >= req_freq:
                    output.add(tuple(sorted([p,q,r])))


        return [list(x) for x in output]