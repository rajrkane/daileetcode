class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Time:   O(n)
        Space:  O(n)
        """
        ret = [0 for _ in nums]
        l, r = 0, n 
        for i in range(n):
            ret[2*i] = nums[l]
            ret[2*i+1] = nums[r]
            l += 1
            r += 1
        return ret 
