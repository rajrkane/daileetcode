# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time:   O(n)
        Space:  O(n)
        """
        def DFS(node, low, high) -> bool:
            if not node:
                return True 

            if node.val <= low or node.val >= high:
                return False 

            return DFS(node.left, low, node.val) and DFS(node.right, node.val, high)

        return DFS(root, -float("inf"), float("inf"))
