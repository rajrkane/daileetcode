class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Time:   O(n^2)
        Space:  O(n^2)
        """
        n = len(grid)
        ans = -math.inf
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    top = dp[i-1][j] if i > 0 else math.inf
                    left = dp[i][j-1] if j > 0 else math.inf
                    dp[i][j] = min(top, left) + 1
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                bottom = dp[i+1][j] if i < n-1 else math.inf 
                right = dp[i][j+1] if j < n-1 else math.inf
                dp[i][j] = min(bottom + 1, right + 1, dp[i][j])
                ans = max(ans, dp[i][j])
        return ans if (ans > 0 and ans < math.inf) else -1
