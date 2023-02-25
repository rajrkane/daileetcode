class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Approach:   Merge sort 
        Time:       O(n*log(n))
        Space:      O(n)
        """
        n = len(nums)
        if n == 1:
            return nums
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:n]
        self.sortArray(left)
        self.sortArray(right)
        self.merge(left, right, nums)
        return nums

    def merge(self, left: List[int], right: List[int], nums: List[int]):
        l = r = 0
        while l + r < len(nums):
            if r == len(right) or (l < len(left) and left[l] < right[r]):
                nums[l + r] = left[l]
                l += 1
            else:
                nums[l + r] = right[r]
                r += 1
