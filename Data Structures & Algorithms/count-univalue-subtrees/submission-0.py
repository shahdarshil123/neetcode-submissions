# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node):
            if node is None:
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                if node.left and node.left.val != node.val:
                    return False
                
                if node.right and node.right.val != node.val:
                    return False
                
                self.result += 1
                return True
            
            return False
        
        dfs(root)

        return self.result