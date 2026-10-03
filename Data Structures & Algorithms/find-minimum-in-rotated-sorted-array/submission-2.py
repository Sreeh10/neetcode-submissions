class Solution:
    def findMin(self, nums: List[int]) -> int:

        # binary search on answer:
        # minimum element is the only one less than it's prev cyclar element, because it is a sorted array
        
        # check the edge case, if no rotation (also covers the case when there is only 1 element in the array)
        if nums[0] <= nums[-1]:
            return nums[0]

        space = (0, len(nums)-1)

        limit = 10
        while space[0] <= space[1] and limit > 0:
            # print(space)
            limit -= 1
    
            middle = (space[0] + space[1]) // 2 # left middle in case of even
            # check if middle element is min:
            if nums[middle-1] > nums[middle] and nums[(middle+1)%len(nums)] > nums[middle]:
                return nums[middle]
            if nums[middle] >= nums[0]: # fall is yet to occur
                # check right half
                space = (middle+1,space[1])
            if nums[middle] < nums[0] : # fall has occured somewhere to left already
                #  check left half
                space = (space[0], middle-1)
        
        return nums[middle]
        
        