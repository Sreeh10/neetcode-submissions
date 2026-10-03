# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if fast is None:
            return False
        if fast.next is None:
            return False 
        while True:

            slow = slow.next
            fast = fast.next.next

            if fast is None or fast.next is None:
                return False
            
            if slow.val == fast.val:
                return True
        

        return False
