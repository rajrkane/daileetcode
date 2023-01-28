class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        Approach:   Use collections.deque as it is implemented as a DLL
        Time:       O(k*n)
        Space:      O(n)
        '''
        q = collections.deque(range(n, 0, -1))
        while len(q) > 1:
            for _ in range(k-1):
                q.appendleft(q.pop())
            q.pop()
        return q[0]
