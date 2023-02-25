class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time:   O(m * n)
        Space:  O(m + n)
        """
        def dfs(node: TreeNode) -> bool:
            if node is None:
                return False 
            
            if isIdentical(node, subRoot):
                return True 

            return dfs(node.left) or dfs(node.right)

        def isIdentical(s: TreeNode, t: TreeNode) -> bool:
            if s is None or t is None:
                return s is None and t is None
            
            return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
                
        return dfs(root)
