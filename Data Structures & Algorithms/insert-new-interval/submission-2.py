
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        ans = []
        len_x = newInterval[1] - newInterval[0]
        appended = False
        for i in range(len(intervals)):
            len_i = intervals[i][1] - intervals[i][0] 
            # print(len_i, len_x, newInterval, ans)
            if (len_i + len_x) >= (max(intervals[i]+ newInterval) - min(intervals[i] + newInterval)):
                # merge
                newInterval = [min(intervals[i] + newInterval),max(intervals[i]+ newInterval)]
                len_x = newInterval[1] - newInterval[0]
            else:
                if intervals[i][0] > newInterval[0] and (not appended):
                    ans.append(newInterval)
                    appended = True
                ans.append(intervals[i])
        
        if not appended:
            ans.append(newInterval)
        return ans

        