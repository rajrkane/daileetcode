class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Time:   O(n*k)
        Space:  O(1) excluding the return array
        '''
        ans = []
        for i in range(0, len(nums) - k + 1):
            ans.append(max(nums[i:i+k]))
        return ans 

        '''
        Time:   O(n)
        Space:  O(k) excluding the return array
        '''
        # monotonically decreasing queue (of indices)
        # max_q[0] -> greatest, max_q[-1] -> smallest
        max_q = collections.deque()
        ans = []
        l = r = 0

        while r < len(nums):
            # remove smaller values from queue 
            while max_q and nums[max_q[-1]] < nums[r]:
                max_q.pop()
            max_q.append(r)

            # remove if out of window
            if max_q[0] < l:
                max_q.popleft()
            
            # we start finding answers once we have a large enough window
            if r + 1 >= k:
                ans.append(nums[max_q[0]])
                l += 1

            r += 1

        return ans 
