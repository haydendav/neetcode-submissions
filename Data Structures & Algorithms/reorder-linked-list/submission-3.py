# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = head
        tail = head.next

        while tail and tail.next: #find middle
            middle = middle.next
            tail = tail.next.next

        curr = middle.next
        prev = None
        middle.next = None

        while curr: #reverse from middle
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        starttail = head
        endtail = prev

        while starttail and endtail: #assign start middle back and forth
            temp1 = starttail.next
            temp2 = endtail.next
            starttail.next = endtail
            endtail.next = temp1
            starttail = temp1
            endtail = temp2

        
        