class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # assume you make an n x n grid, with the same array as row x column
        # start at 0,0 , if you want to pick element i, step down; and if skipping step right
        # you want to reach the as deep as possible down
        # you can never go to the right of principal diagonal, because you cant skip more than i elements within the first i elements

        # dp[i][j] = smallest possible value of ending elem of j-length subsequence within first i elements of array
        try:
      
            dp = [[None for j in range(len(nums)+1)] for i in range(len(nums))]
            # smallest possible end value of 1-length sequence is the cumulative minimum
            cum_min = nums[0]
            for i in range(len(nums)):
                cum_min = min(cum_min, nums[i])
                dp[i][1] = cum_min

            for i in range(1,len(nums)):
                for j in range(2,i+2):
                    # print(i, j, end = " ")
                    if dp[i-1][j] is not None:
                        # print("A",end="")
                        if dp[i-1][j-1] is not None:
                            # print("A",end="")
                            if nums[i] > dp[i-1][j-1]:
                                # print("A", end="")
                                dp[i][j] = min(dp[i-1][j], nums[i])
                            else:
                                # print("B", end="")
                                dp[i][j] = dp[i-1][j]

                    else:
                        # print("B", end="")
                        if dp[i-1][j-1] is not None:
                            # print("A", end="")
                            if nums[i] > dp[i-1][j-1]:
                                # print("A",end="")
                                dp[i][j] = nums[i]
                    # print("x")

            # for arr in dp:
                # print(arr)
            for j in range(len(nums), 0, -1):
                if dp[-1][j] is not None:
                    return j
        except:
            print(i,j)
            for arr in dp:
                print(arr)

        