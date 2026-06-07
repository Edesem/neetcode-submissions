# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 1
        i = head
        j = head
        prev = head
        start = j

        while i.next:
            i = i.next
            length += 1
        
        pos = 1
        while pos != length - n + 1:
            prev = j
            j = j.next
            pos += 1
        
        print(prev.val, j.next)
        if pos == 1:
            head = j.next
        else:
            prev.next = j.next
        return head


