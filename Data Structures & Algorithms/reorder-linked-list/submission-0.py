from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        queue = deque()
        stack = deque()
        count = 0
        while head is not None:
            queue.append(head)
            stack.append(head)
            count += 1
            head = head.next

        # print([x.val for x in queue])
        # print([x.val for x in stack])

        saved_head = head
        curr = queue.popleft()
        count -= 1

        while count > 0:

            if len(stack) > 0:
                curr.next = stack.pop()
                count -= 1
                curr = curr.next
            if len(queue) > 0:
                curr.next = queue.popleft()
                count -= 1
                curr = curr.next

        
        curr.next = None
        return saved_head
        
