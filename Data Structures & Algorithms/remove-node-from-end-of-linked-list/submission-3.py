# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        tail = head
        target = head
        prev = head

        while tail.next:
            tail = tail.next
            length += 1
        
        pos = 1
        while pos != length - n + 1:
            prev = target
            target = target.next
            pos += 1
        
        if pos == 1:
            head = target.next
        else:
            prev.next = target.next
        return head


