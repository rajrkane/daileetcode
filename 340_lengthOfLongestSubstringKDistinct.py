class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        Time:   O(n)
        Space:  O(k)
        '''
        if k == 0:
            return 0
        l = r = 0
        last_seen = {s[0]: 0}
        cur_max = 1
        while r < len(s):
            last_seen[s[r]] = r
            r += 1
            if len(last_seen) == k + 1:
                oldest = min(last_seen.values())
                last_seen.pop(s[oldest])
                l = oldest + 1
            cur_max = max(cur_max, r - l)
        return cur_max
