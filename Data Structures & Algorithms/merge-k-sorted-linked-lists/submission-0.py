# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # maintain a heap of front nodes of each list
        # heapify fronts : O(K)
        # for each n , heap push O(log K)
        # total O(K + n logK)

        h = []
        heapq.heapify(h) # min heap
        for i,l in enumerate(lists):
            if l is not None: # skip empty lists
                heapq.heappush(h, (l.val, i)) # each heap element is a tuple (frontval, list-index)

        saved_head = ListNode() 
        curr = saved_head
        while len(h) > 0:
            val, indx = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[indx].next is not None:
                lists[indx] = lists[indx].next
                heapq.heappush(h, (lists[indx].val,indx))
        
        return saved_head.next