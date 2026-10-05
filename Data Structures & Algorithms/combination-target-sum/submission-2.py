from collections import deque
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        q = deque()
        q.append((0, [])) # (sum, combination)
        ans = set()
        iter_limit = 20
        while len(q) > 0 and iter_limit > 0:
            sum_, combination_ = q.popleft()
            for n in nums:
                if len(combination_) == 0 or n <= combination_[0]: # keep combination always sorted already
                    if sum_ + n == target:
                        ans.add(tuple([n] + combination_))
                    elif sum_ + n < target:
                        q.append((sum_ + n, [n] + combination_))
                    else: # sum greater than target, simply discard
                        pass

            # if sum_ + 10 >= target:
            #     print([x for x in q])
            #     print([list(a) for a in ans])
            # iter_limit -= 1


        return [list(a) for a in ans]
        