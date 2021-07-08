# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        for i in range(n):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        
        return dummy.next
        """if head.next==None and n==1:
            return None
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        
        temp=head
        i=0
        count=count-n
        if count==0:
            head=head.next
        while temp:
            i+=1
            if i==count:
                if temp.next and temp.next.next:
                    temp.next=temp.next.next
                else:
                    temp.next=None
                
            temp=temp.next
        return head
                """
                
            
        