# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        """
        Approach:   2 Stacks
        Time:       O(n)
        Space:      O(n)
        """
        if root is None:
            return []
        ltr = [root]
        rtl = []
        level = []
        traversal = []
        while ltr or rtl:
            while ltr:
                node = ltr.pop()
                level.append(node.val)
                if node.left:
                    rtl.append(node.left)
                if node.right:
                    rtl.append(node.right)
            traversal.append(level)
            level = []
            while rtl:
                node = rtl.pop()
                level.append(node.val)
                if node.right:
                    ltr.append(node.right)
                if node.left:
                    ltr.append(node.left)
            if level:
                traversal.append(level)
            level = []
        return traversal

