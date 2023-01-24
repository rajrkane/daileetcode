class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Time:   O(m*n)
        Space:  O(m*n)
        '''
        if m == 1 or n == 1:
            return 1
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, n):
            paths[0][i] = 1
        for i in range(1, m):
            paths[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]

        '''
        Time:   O(m*n)
        Space:  O(n)
        '''
        if m == 1 or n == 1:
            return 1
        prev_row = [1 for _ in range(n)]
        prev_row[0] = 0
        for i in range(1, m):
            cur_row = [1 for _ in range(n)]
            for j in range(1, n):
                cur_row[j] = cur_row[j-1] + prev_row[j]
            prev_row = cur_row
        return prev_row[-1]
