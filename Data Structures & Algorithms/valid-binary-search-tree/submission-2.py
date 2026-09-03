# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = -float('inf')
        right = float('inf')

        def dfs(node, left, right):
            if node is None:
                return True
            
            if not left < node.val < right:
                return False
            
            if not dfs(node.left, left, min(right, node.val)):
                return False

            if not dfs(node.right, max(left, node.val), right):
                return False
            
            return True
        
        return dfs(root,left, right)
            
