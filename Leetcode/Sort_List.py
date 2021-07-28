# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        """ temp=head               #O(nlogn) and O(n) space
        lis=[]
        while temp:
            lis.append(temp.val)
            temp=temp.next
        #print(lis)
        lis.sort()
        temp=head
        i=0
        while temp:
            temp.val=lis[i]
            temp=temp.next
            i+=1
        return head"""