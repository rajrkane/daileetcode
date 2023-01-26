class Solution:
    def numSplits(self, s: str) -> int:
        '''
        Time:   O(n)
        Space:  O(n)
        '''
        # count unique characters left to right
        seen = set()
        ltr = [0 for _ in s]
        ltr[0] = 1
        seen.add(s[0])
        for i in range(1, len(s)):
            ltr[i] = ltr[i-1]
            if s[i] not in seen:
                ltr[i] += 1
                seen.add(s[i])

        # count unique characters right to left
        seen = set()
        rtl = [0 for _ in s]
        rtl[-1] = 1
        seen.add(s[-1])
        for i in range(len(s)-2, -1, -1):
            rtl[i] = rtl[i+1]
            if s[i] not in seen:
                rtl[i] += 1
                seen.add(s[i])

        # at every potential split, check if left count matches right count
        splits = 0
        for i in range(len(s)-1):
            if ltr[i] == rtl[i+1]:
                splits += 1
        return splits
