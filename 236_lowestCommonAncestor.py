class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time:   O(n)
        Space:  O(log(n)) to O(n)
        """
        if root is None:
            return None 
        if root == p or root == q:
            return root
        ancestor_left = self.lowestCommonAncestor(root.left, p, q)
        ancestor_right = self.lowestCommonAncestor(root.right, p, q)
        if ancestor_left and ancestor_right:
            return root 
        return ancestor_left or ancestor_right
