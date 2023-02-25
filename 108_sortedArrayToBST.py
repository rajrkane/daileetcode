class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Time:   O(n)
        Space:  O(n)
        """
        def helper(start: int, end: int) -> TreeNode:
            if start >= end:
                return None  
            mid = (start + end) // 2
            return TreeNode(
                val = nums[mid],
                left = helper(start, mid),
                right = helper(1+mid, end)
            )

        return helper(0, len(nums))
