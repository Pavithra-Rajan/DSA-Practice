# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.tot=self.sum_all(root)
        self.new_val(root)
        return root
        
    def new_val(self,root):
        if not root:
            return 
        self.new_val(root.left)
        old=root.val
        root.val=self.tot
        self.tot-=old
        self.new_val(root.right)
        
    def sum_all(self,root):
        if not root:
            return 0
        if not(root.left or root.right):
            return root.val
        return root.val+self.sum_all(root.left)+self.sum_all(root.right)