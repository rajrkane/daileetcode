class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Time:   O(n*m)
        Space:  O(m)
        '''
        fewest = [amount + 1 for _ in range(amount + 1)]
        fewest[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                diff = amt - coin 
                if diff >= 0:
                    fewest[amt] = min(fewest[amt], fewest[diff] + 1)
        return fewest[-1] if fewest[-1] <= amount else -1
