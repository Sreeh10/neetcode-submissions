def find_min_index(nums: List[int]) -> int:
    if nums[0] <= nums[-1]:
        return 0
    
    space = (0, len(nums)-1)

    while space[0] <= space[1]:
        print(f"mindexspace={space}")
        middle = (space[0] + space[1]) // 2
        if nums[middle] < nums[middle-1] :
            return middle 
        if nums[middle] >= nums[0]: # middle is in hill 1, look right half
            space = (middle + 1, space[1])
        else: # middle is in hill 2, look left half
            space = (space[0], middle-1)
    
    return middle

def binary_search(nums, target):
    if target > nums[-1] or target < nums[0]:
        return -1
    space = (0, len(nums)-1)
    while space[0] <= space[1]:
        print(f"binspace={space}")
        middle = (space[0] + space[1]) //2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            space = (space[0], middle-1)
        else:
            space = (middle+1, space[1]) 
    return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find min, then do 0 to min-1, min to end
        space = (0, len(nums)-1)
        mindex = find_min_index(nums)
        print(f"{mindex=}")
        
        if target >= nums[0]: #search in hill 1
            space = (0,(mindex-1)%(len(nums)))
        else: # search in hill 2 
            space = (mindex, len(nums)-1 )

        print(f"{space[0]}+:")
        x = binary_search(nums[space[0] : space[1]+1] , target)
        return (space[0] + x) if x != -1 else x
