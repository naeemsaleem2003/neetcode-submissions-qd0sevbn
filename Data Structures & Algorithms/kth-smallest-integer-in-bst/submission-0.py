# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        result = root.val
        def dfs(node):
            nonlocal counter, result
            if not node:
                return 0
            dfs(node.left)
            counter -= 1
            if counter == 0:
                result = node.val
                return result
            dfs(node.right)
        dfs(root)
        return result