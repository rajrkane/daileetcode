class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        Time:   O(n)
        Space:  O(1), since last_seen holds at most three keys
        '''
        l = r = 0
        last_seen = {s[0]: 0}
        cur_max = 1
        while r < len(s):
            last_seen[s[r]] = r
            r += 1
            if len(last_seen) == 3:
                # pop the least recently seen 
                oldest = min(last_seen.values())
                last_seen.pop(s[oldest])
                l = oldest + 1
            cur_max = max(cur_max, r - l )
        return cur_max

