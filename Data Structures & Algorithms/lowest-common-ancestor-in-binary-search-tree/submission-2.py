# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp

        def dfs(node, p, q):
            if node is None:
                return

            if node.val == p or node.val == q:
                return node
            elif p < node.val < q:
                return node
            
            elif p < node.val and q < node.val:
               return dfs(node.left,p,q)
            
            else:
                return dfs(node.right, p, q)
        
        return dfs(root,p.val,q.val)
            