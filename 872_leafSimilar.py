class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Time:   O(n+m)
        Space:  O(max(log(n), log(m))) to O(max(n, m))
        """
        seq = []

        def dfs(node: TreeNode):
            if not node.left and not node.right:
               seq.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root1)
        dfs(root2)
        print(seq)
        return seq[:len(seq)//2] == seq[len(seq)//2:] 
