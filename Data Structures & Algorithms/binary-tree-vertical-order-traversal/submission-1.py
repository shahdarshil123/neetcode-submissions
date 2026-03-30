# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        left = 0
        right = 0
        curr = 0
        hmap = {0:[]}

        queue = collections.deque()
        queue.append((root,curr))

        while queue:
            node, curr = queue.popleft()
            if curr not in hmap:
                hmap[curr] = []
            hmap[curr].append(node.val)
            if node.left:
                if curr-1 < left:
                    left = curr-1
                queue.append((node.left,curr-1))
            if node.right:
                if curr+1 > right:
                    right = curr+1
                queue.append((node.right, curr+1))
        
        result = []
        for i in range(left, right+1):
            result.append(hmap[i])
        
        return result
            
            
            
