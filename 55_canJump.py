class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
		Approach:	Dynamic programming
        Time:   	O(n*k) where k is max(nums)
        Space:  	O(n)
        '''
        # if len(nums) == 1:
        #     return True
        # # track whether last index can be reached from each index 
        # dp = [False for _ in nums]
        # dp[-1] = True 
        # for i in range(len(nums) - 2, -1, -1):
        #     j = min(nums[i], len(nums) - i - 1)
        #     while (not dp[i]) and j > 0:
        #         if dp[i+j]:
        #             dp[i] = True 
        #         j -= 1
        # return dp[0]

        '''
		Approach:	Greedy
        Time:   	O(n)
        Space:  	O(1)
        '''
        # smarter tracking of good positions
        # see if we can jump from the current index to the leftmost good index (going right to left)
        if len(nums) == 1:
            return True 
        last_good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= last_good - i:
                last_good = i 
        # finally, the result is whether the leftmost good index is the start of the array
        return last_good == 0
