# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        # {0, 1} {1, 2} {2, 3} {3, None}
        # {0, None} {} 
        while (head is not None):
            next = head.next # next = 1
            head.next = prev # {0, None}
            prev = head # prev = 0
            head = next # head = 1
            # x = head
            # while(x != None):
                # print(x.val)
                # x = x.next

        return prev
        