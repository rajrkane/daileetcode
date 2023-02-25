class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time:   O(h)
        Space:  O(h)
        """
        traversal = []
        if root:
            traversal = self.inorderTraversal(root.left)
            traversal.append(root.val)
            traversal.extend(self.inorderTraversal(root.right))
        return traversal 
