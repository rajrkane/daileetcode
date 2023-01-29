class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Approach:   Dynamic programming
        Time:       O(n^2)
        Space:      O(n)
        '''
        if len(nums) == 1:
            return 0
        dp = [len(nums) for _ in nums]
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            max_step = min(nums[i], len(nums) - i - 1)
            for j in range(max_step, 0, -1):
                dp[i] = min(dp[i], dp[i+j] + 1)
        return dp[0]

        '''
        Approach:   Greedy / BFS
        Time:       O(n)
        Space:      O(1)
        '''
        count = 0
        l = r = 0
        while r < len(nums) - 1:
            # track the farthest jump possible from within the window
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # update window 
            l = r + 1
            r = farthest
            # increment count for each jump (ie for each window update)
            count += 1
            
        return count 

