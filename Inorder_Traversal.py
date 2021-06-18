# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        def trav(root):
            if not root:
                return 
            trav(root.left)
            # print(root.val)
            stack.append(root.val)
            trav(root.right)
        trav(root)
        return stack