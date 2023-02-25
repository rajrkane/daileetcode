class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Time:   O(n)
        Space:  O(log(n)) to O(n)
        """
        sums = set([])

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            nodeSum = dfs(node.left) + dfs(node.right) + node.val 
            sums.add(nodeSum)
            return nodeSum 
        
        total = dfs(root)
        best = 0
        for s in sums:
            best = max(best, s * (total - s))
        
        return best % (10**9 + 7)
