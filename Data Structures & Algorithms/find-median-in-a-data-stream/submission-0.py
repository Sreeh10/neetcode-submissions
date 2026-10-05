import heapq

class MedianFinder:
    # we'll always make sure left_count <= right_count + 1 and right_count <= left_count
    def __init__(self):
        # left is max heap, at anytime, we should be able to transfer the max elem to the right, to balance counts
        self.left = []
        heapq.heapify_max(self.left)

        #right is min heap
        self.right = []
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if (m:=self.findMedian()) is None or  num < m:
            heapq.heappush_max(self.left, num) # log(n)
            if len(self.left) > len(self.right) + 1: # if imbalanced, then balance it
                heapq.heappush(self.right, heapq.heappop_max(self.left))
        else:
            heapq.heappush(self.right, num) # log(n)
            if len(self.left) < len(self.right):
                heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == 0 and len(self.right) == 0:
            return None
        if len(self.left) == 0:
            return self.right[0]
        if len(self.right) == 0:
            return self.left[0]

        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0])/2
        else:
            return self.left[0]
        # maintain 2 heaps
        # one for the left half and one for the right half of elements so far
        # both trees must be balanced at all times
        # if a new number

        
        