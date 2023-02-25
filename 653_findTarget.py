class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Time:   O(n)
        Space:  O(n)
        """
        vals = set()
        visited = collections.deque([root])
        while visited:
            node = visited.popleft()
            if k - node.val in vals:
                return True
            vals.add(node.val)
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)
        return False 
