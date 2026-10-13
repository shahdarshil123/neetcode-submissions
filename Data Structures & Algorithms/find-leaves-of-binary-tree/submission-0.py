# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        self.height_group = collections.defaultdict(list)
        
        def dfs(node):
            if node is None:
                return 0
            height = max(dfs(node.left), dfs(node.right))
            self.height_group[height].append(node.val)
            return 1 + height
        
        dfs(root)

        result = []
        height = 0
        while height in self.height_group:
            result.append(self.height_group[height])
            height += 1
        
        return result
