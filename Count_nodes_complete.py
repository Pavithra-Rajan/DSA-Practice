# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def lh(root):
            if not root:
                return 0
            return 1+lh(root.left)
        def rh(root):
            if not root:
                return 0
            return 1+rh(root.right)
        l,r=lh(root),rh(root)
        if l==r:
            return 2**l-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        #linear time
        """if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)"""