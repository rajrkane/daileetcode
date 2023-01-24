class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        '''
        Time:   O(n^2)
        Space:  O(1)
        '''
        sdp = 0
        cur = 0
        p = len(prices)
        for i in range(1, p):
            if prices[i-1] - prices[i] == 1:
                cur += 1
            else:
                sdp += sum(range(cur+1))
                cur = 0
        sdp += sum(range(cur+1))
        sdp += p 
        return sdp
      
        '''
        Time:   O(n)
        Space:  O(1)
        '''
        def sum_n(n: int) -> float:
            return n * (n + 1) / 2

        sdp = 0
        cur = 0
        p = len(prices)
        for i in range(1, p):
            if prices[i-1] - prices[i] == 1:
                cur += 1
            else:
                sdp += sum_n(cur)
                cur = 0
        sdp += sum_n(cur)
        sdp += p 
        return int(sdp)
