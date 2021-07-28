# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if k==0:
            return head
        
        temp=head
        size=0
        while temp:
            size+=1
            if temp.next is None:
                end=temp
            temp=temp.next

        if k!=0:
            k=k%size
        if k==0:
            return head
        
        count=0
        temp=head
        while temp:
            count+=1
            if count==size-k:
                #print("in end")
                start=temp.next
                temp.next=None
            temp=temp.next
            
        end.next=head
        head=start
        return head
     
        
        