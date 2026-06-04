# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        restail = res
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                restail.next = curr1
                restail = curr1
                curr1 = curr1.next
            else:
                restail.next = curr2
                restail = curr2
                curr2 = curr2.next

        if curr1:
            restail.next = curr1
        elif curr2:
            restail.next = curr2
        
        return res.next 

        