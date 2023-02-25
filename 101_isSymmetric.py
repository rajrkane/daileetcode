class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Time:   O(h)
        Space:  O(h)
        """
        def isSym(left: TreeNode, right: TreeNode) -> bool:
            if left and right and left.val == right.val:
                return isSym(left.left, right.right) and isSym(left.right, right.left)
            return left == right 
        return isSym(root.left, root.right)
