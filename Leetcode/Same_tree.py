# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p and q and p.val!=q.val:
            return False
        if p and q:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        """def preorder(root,ls):
            if root:
                ls.append(root.val)
                preorder(root.left,ls)
                preorder(root.right,ls)
            else:
                ls.append(-9999)
        pl=[]
        ql=[]
        preorder(p,pl)
        preorder(q,ql)
        return pl==ql"""
        