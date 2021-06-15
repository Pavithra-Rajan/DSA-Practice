# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #  iterative
        """stack=[root]
        while stack:
            temp=stack.pop()
            if temp:
                temp.left,temp.right=temp.right,temp.left
                stack+=temp.left,temp.right
        return root"""
        # recursive
        """if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root"""
            
        