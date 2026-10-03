class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0 -> without robbing first house, without robbing current house
        # 1 -> without robbing first house, with robbing current house
        # 2 ->  with robbing first house, without robbing current house
        # 3 ->  with robbing first house, with robbing current house
        dp = [[0, -1, -1, nums[0]]]
        if len(nums) > 1:
            dp.append ( [0, nums[1], nums[0], -1])
            if len(nums) > 2:
                dp.append ( [nums[1], nums[2], nums[0], nums[0] + nums[2]] )

                print(dp)
                for i in range (3,len(nums)):
                    dp.append(
                        [
                            max(dp[i-1][0], dp[i-1][1]),
                            dp[i-1][0] + nums[i],
                            max(dp[i-1][2], dp[i-1][3]),
                            dp[i-1][2] + nums[i]
                        ]
                    )
            else:
                return max(nums)
        else:  
            return nums[0]
        print(dp)
        return max(dp[-1][0], dp[-1][1], dp[-1][2])
        
        