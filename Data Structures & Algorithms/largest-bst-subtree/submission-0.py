# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0
    
        def dfs(node):
            if node is None:
                return [True, float('inf'), -float('inf'), 0]
            
            left_check, left_min, left_max, left_sz = dfs(node.left)
            right_check, right_min, right_max, right_sz = dfs(node.right)

            if left_check and right_check and left_max < node.val < right_min:
                sz = 1 + left_sz + right_sz
                self.max_count = max(self.max_count, sz)
                return [True, min(left_min, node.val), max(right_max, node.val), sz]
            else:
                return [False, 0, 0, 0]
        
        dfs(root)
        return self.max_count