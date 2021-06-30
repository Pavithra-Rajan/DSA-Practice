# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp=head
        while temp:
            if temp.next and temp.next.val==temp.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        