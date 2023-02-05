class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Time:   O(n+m)
        Space:  O(1), since limited to 26 character alphabet
        """
        goal = {chr(char):0 for char in range(ord("a"), ord("a")+26)}
        for char in p:
            goal[char] += 1
        ans = []

        l = r = 0
        cur = {chr(char):0 for char in range(ord("a"), ord("a")+26)}
        while r < len(s):
            if goal[s[r]] == 0:
                # not looking for this char, RESET the window
                i = l 
                for i in range(l, r+1):
                    cur[s[i]] = 0
                l = r + 1
                r += 1
                continue

            if cur[s[r]] == goal[s[r]]:
                # already have enough of this char (> 0), CONTRACT the window 
                cur[s[l]] -= 1
                l += 1
                continue

            # consider window with this char 
            cur[s[r]] += 1

            if r - l + 1 < len(p):
                # need more characters, EXPAND the window 
                r += 1
                continue 

            # window is size of p
            if cur == goal:
                # found answer, SLIDE the window 
                ans.append(l)
                cur[s[l]] -= 1
                l += 1
                r += 1
            else:
                cur[s[l]] -= 1
                l += 1

        return ans 
