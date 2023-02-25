class Solution:
    def numTrees(self, n: int) -> int:
        """
        Approach:   Catalan numbers using dynamic programming
        Time:       O(n^2)
        Space:      O(n)
        """
        C = [0 for _ in range(n+1)]
        C[0] = 1
        C[1] = 1
        for i in range(2, n+1):
            l, r = 0, i - 1
            for j in range(i):
                C[i] += C[l] * C[r]
                l += 1
                r -= 1 

        return C[-1]

        """
        Approach:   Catalan number using formula
        Time:       O(n)
        Space:      O(1)
        """
        C = 1
        for i in range(1, n):
            C = C * 2*(2*i + 1) / (i + 2)
        return int(C)

