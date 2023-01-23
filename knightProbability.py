class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        '''
        Approach:   Dynamic programming
        Time:       O(k*n^2)
        Space:      O(n^2)
        '''
        # dp[r][c] is prob of being on cell (r, c) after a certain number of moves 
        # initial state is that the knight can only be on (row, column)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1
        # possible directions that a knight can move 
        moves = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2), (-2, 1), (-1, 2)]
        for _ in range(k):
            # the dp matrix for the next move 
            next_dp = [[0 for _ in range(n)] for _ in range(n)]
            # iterate over the previous dp matrix 
            for r in range(n):
                for c in range(n):
                    # take each of the 8 moves from each cell of the previous dp matrix 
                    for dr, dc in moves:
                        # if we end up on a new cell, update its probability 
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            # add dp[r][c] because we are going to new cell from (r, c)
                            # normalized by number of moves possible 
                            next_dp[r+dr][c+dc] += dp[r][c] / 8.0
            dp = next_dp
        total_prob = 0
        for r in dp:
            total_prob += sum(r)
        return total_prob
