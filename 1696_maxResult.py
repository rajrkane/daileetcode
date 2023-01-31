class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
        Time:   O(n), since each element is pushed/popped only once 
        Space:  O(n+k)
        '''
        # dp[i] is max score possible ending at index i 
        score = [0 for _ in nums]
        score[0] = nums[0]

        # monotonically decreasing queue (stores indices pointing to values)
        max_q = collections.deque()
        max_q.append(0)

        for i in range(1, len(nums)):
            # pop indices that are more than k away
            while max_q and max_q[0] < i - k:
                max_q.popleft()
            
            # max score ending at i is value at i + previous max score (after updating queue)
            score[i] = nums[i] + score[max_q[0]]

            # don't need to consider indices whose score is smaller
            while max_q and score[max_q[-1]] < score[i]:
                max_q.pop()
            
            max_q.append(i)            

        return score[-1]
