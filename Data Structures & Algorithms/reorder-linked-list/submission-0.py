# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = head
        j = head
        prev = j

        while i.next:
            while j.next:
                prev = j
                j = j.next

            if i.next == j:
                return

            temp = i.next
            i.next = j
            prev.next = None
            i = temp
            j.next = i
            j = i