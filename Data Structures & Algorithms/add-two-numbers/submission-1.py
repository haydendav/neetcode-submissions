# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""
        
        while l1:
            first = str(l1.val) + first
            l1 = l1.next

        while l2:
            second = str(l2.val) + second
            l2 = l2.next

        total = int(first) + int(second)
        strTotal = str(total)


        l3 = ListNode()
        curr = l3
        for char in reversed(strTotal):
            curr.next = ListNode(int(char))
            curr = curr.next

        return l3.next


        