# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time:   O(n)
        Space:  O(log(n)) to O(n)
        """
        def subtreeHasOne(node) -> bool:
            if not node:
                return False # determined no 1 in this subtree 
            leftHasOne = subtreeHasOne(node.left)
            if not leftHasOne:
                node.left = None 
            rightHasOne = subtreeHasOne(node.right)
            if not rightHasOne:
                node.right = None 
            # returning node.val here works because each node.val is either 0 or 1
            return node.val or leftHasOne or rightHasOne 
            
        return root if subtreeHasOne(root) else None 
