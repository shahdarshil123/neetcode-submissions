# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.result = 0
        def dfs(node, val):
            if node is None:
                return
            
            if node.val >= val:
                self.result += 1
            
            dfs(node.left, max(node.val, val))
            dfs(node.right, max(node.val, val))

        dfs(root,root.val)
        return self.result