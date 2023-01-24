class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        Time:   O(n)
        Space:  O(n)
        '''
        if len(s) == 1:
            return 0
        dp = [0 for _ in range(len(s))]
        ones = int(s[0])
        for i in range(1, len(s)):
            if int(s[i]) == 1:
                ones += 1
                dp[i] = dp[i-1]
            else:
                dp[i] = min(ones, dp[i-1] + 1)
        return dp[-1]

        '''
        Time:   O(n)
        Space:  O(1)
        '''
        if len(s) == 1:
            return 0
        ans = 0
        ones = int(s[0])
        for i in range(1, len(s)):
            if int(s[i]) == 1:
                ones += 1
            else:
                ans = min(ones, ans + 1)
        return ans
