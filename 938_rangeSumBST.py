# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def DFS(node) -> int:
            if not node:
                return 0
            if node.val < low:
                return DFS(node.right)  
            elif node.val == low:
                return node.val + DFS(node.right) 
            elif node.val > low and node.val < high: 
                return node.val + DFS(node.left) + DFS(node.right)
            elif node.val == high:
                return node.val + DFS(node.left)
            elif node.val > high:
                return DFS(node.left)

        return DFS(root) 
