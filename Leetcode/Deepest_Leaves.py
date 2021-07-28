# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        stack=[root]
        while stack:
            sum_=0
            
            for i in range(len(stack)):
                temp=stack.pop(0)
                sum_+=temp.val
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
             #print(sum_)       
            
            
        return sum_
            
        