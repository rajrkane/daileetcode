class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Time:   O(n+m)
        Space:  O(n+m)
        '''
        # track the min window 
        left, right = 0, float("inf")
        # track the current window
        l = r = 0
        # track the counts of T and the window 
        t_counts = collections.Counter(t)
        wind_counts = collections.defaultdict(int)
        # track how many of required characters are in the window 
        want = len(t_counts)
        have = 0
        while r < len(s):
            wind_counts[s[r]] += 1
            if wind_counts[s[r]] == t_counts[s[r]]:
                have += 1
            while l <= r and have == want:
                if r - l < right - left:
                    left, right = l, r 
                if wind_counts[s[l]] == t_counts[s[l]]:
                    have -= 1
                wind_counts[s[l]] -= 1
                l += 1
            r += 1
        return "" if right == float("inf") else s[left:right+1]
        
