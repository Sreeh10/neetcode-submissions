# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # build an n+1 length stick
        # move the stick until it right end touches list end
        # then bypass from the node at left end 

        right = head
        left = head
        prev2left = left
        count = 1
        while count < n: # n is guaranteed to be less than the size of the list
            right = right.next # right.next is never none when count < size of the list
            count += 1
        
        
        while right.next is not None:
            right = right.next
            count += 1
            prev2left = left
            left = left.next
        
        if count == n:
            return head.next
        else:
            prev2left.next = left.next

        return head