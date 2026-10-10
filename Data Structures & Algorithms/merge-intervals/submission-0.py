class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()
        # rolling = [intervals[0][0], intervals[0][1]]
        rolling = None
        for i in intervals:
            # print(f"{ans=}, {rolling=}, {i=}")
            if rolling is None:
                rolling = i
                continue
            if rolling[1] < i[0]:
                ans.append(rolling)
                rolling = i
                continue
            if rolling[0] > i[1]:
                ans.append(i)
                rolling = None
                continue
            rolling = [min(rolling[0], i[0]), max(rolling[1],i[1])]
        
        if rolling is not None:
            ans.append(rolling)

        return ans
