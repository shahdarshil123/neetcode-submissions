# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.result = root.val


        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, node.val, node.val + left, node.val + right, node.val + left + right)

            return max(node.val, node.val + left, node.val + right)
        
        dfs(root)
        return self.result
            