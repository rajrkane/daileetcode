class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        Approach:   2 monotonic queues (deque) to store max and min of sliding window 
        Time:       O(n) amortized
        Space:      O(n)
        '''
        max_q = collections.deque([0]) # queues store indices
        min_q = collections.deque([0])
        start = 0 # start of sliding window
        ans = 1

        for i in range(1, len(nums)):
            # put the current number in the right place in both queues 
            # max_q is greatest -> smallest 
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i)
            # min_q is smallest -> greatest
            while min_q and nums[min_q[-1]] > nums[i]:
                min_q.pop()
            min_q.append(i)

            # check the absolute difference extremes of the current window
            # max_q[0] is the max and min_q[0] is the min of the window 
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                start += 1
                # drop any indices that are to the left of the new window 
                if max_q[0] < start:
                    max_q.popleft()
                if min_q[0] < start:
                    min_q.popleft()
            
            # new window may not be the optimal one
            # take the best window
            ans = max(i - start + 1, ans)

        return ans
