class Solution:
    def search(self, nums: List[int], target: int) -> int:
        space = (0,len(nums)-1)

        while space[0] <= space[1]:
            mid = sum(space)//2 # fall left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                space = (space[0], mid-1)
            else:
                space = (mid+1, space[1])
        
        return -1