class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cum_min = [prices[0]]
        for p in prices:
            cum_min = cum_min + [min(cum_min[-1],p)]
        
        rev_cum_max = [prices[-1]]
        for p in prices[::-1]:
            rev_cum_max = [max(rev_cum_max[0],p)] + rev_cum_max
        
        return max( [(rev_cum_max[i] - cum_min[i]) for i in range(len(prices))])


        
        