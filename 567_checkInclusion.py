class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time:   O(n+m)
        Space:  O(1), since limited to 26 character alphabet
        """
        cur = {chr(char):0 for char in range(ord("a"), ord("a")+26)}
        goal = {chr(char):0 for char in range(ord("a"), ord("a")+26)}
        for char in s1:
            goal[char] += 1
        # print(goal)
        for i, char in enumerate(s2):
            # print(i, char, cur)
            cur[char] += 1
            if i >= len(s1):
                cur[s2[i-len(s1)]] -= 1
            if cur == goal:
                return True
        return False 
