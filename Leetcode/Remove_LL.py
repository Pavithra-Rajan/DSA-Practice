# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp=head
        while temp and temp.val==val:
            head=head.next
            temp=head
        while temp:
            if temp.next and temp.next.val==val:
                temp.next=temp.next.next
                continue
            temp=temp.next
        
            
        return head
        