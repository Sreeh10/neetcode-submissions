# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        saved1 = list1
        saved2 = list2
        ans = ListNode()
        saved_ans = ans

        while True: # can use for loop for safety?
            if list1 is None:
                ans.next = list2
                break
            if list2 is None:
                ans.next = list1
                break

            if list1.val < list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        return saved_ans.next