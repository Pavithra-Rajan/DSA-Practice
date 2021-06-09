# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return 0
        fast=head.next
        slow =head
        while fast is not None and slow is not None and fast.next is not None:
            if slow==fast:
                return 1
            fast=fast.next.next
            slow=slow.next
        return 0