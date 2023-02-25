class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time:   O(h)
        Space:  O(h)
        """
        if root:
            visited = collections.deque([root])
            while visited:
                node = visited.popleft()
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
                node.left, node.right = node.right, node.left 
        return root 
