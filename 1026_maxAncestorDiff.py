class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Time:   O(n)
        Space:  O(n)
        """
        def dfs(node: TreeNode, min_anc: int, max_anc: int) -> int:
            if node is None:
                return max_anc - min_anc 

            min_anc = min(min_anc, node.val)
            max_anc = max(max_anc, node.val)
            return max(dfs(node.left, min_anc, max_anc), dfs(node.right, min_anc, max_anc))

        return dfs(root, root.val, root.val)
