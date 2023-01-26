class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        '''
        apples on a pizza??? okay...
        dp[i][j] is how many A's are in submatrix starting at that cell in the pizza
        prefix sum with top-down memoization approach
        Time:   O(n*m*k*(n+m))
        Space:  O(n*m*k)
        '''
        rows = len(pizza)
        cols = len(pizza[0])
        prefix_sum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                is_apple = 1 if pizza[i][j] == "A" else 0
                prefix_sum[i][j] = is_apple + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i+1][j+1]
        for row in prefix_sum:
            print(row)
        
        cache = {} # state (row, column, remaining cuts)
        # given a state, return if it's a valid way of cutting the pizza 
        def recurse(cur_row: int, cur_col: int, cuts_left: int) -> int:
            if (cur_row, cur_col, cuts_left) in cache:
                return cache[cur_row, cur_col, cuts_left]
            # base case: if cut yields piece with no apples, it is invalid
            if prefix_sum[cur_row][cur_col] == 0:
                return 0
            # base case: if no more remaining cuts, found a valid state 
            if cuts_left == 0:
                return 1

            ret = 0
            # iterate over horizontal cuts below cur_row 
            for r in range(cur_row+1, rows):
                # check if the cut is valid, i.e., if both resulting pieces would have an apple
                if prefix_sum[cur_row][cur_col] - prefix_sum[r][cur_col] > 0: 
                    ret += recurse(r, cur_col, cuts_left-1)

            # same for vertical cuts 
            for c in range(cur_col+1, cols):
                if prefix_sum[cur_row][cur_col] - prefix_sum[cur_row][c] > 0:
                    ret += recurse(cur_row, c, cuts_left-1)

            cache[cur_row, cur_col, cuts_left] = ret
            return ret

        return recurse(0, 0, k-1) % (10**9 + 7)
