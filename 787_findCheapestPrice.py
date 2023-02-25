class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Approach:   Bellman-Ford algorithm (sort of BFS)
        Time:       O(k*(n+edges))
        Space:      O(n)
        """
        dist = [math.inf for _ in range(n)]
        dist[src] = 0
        
        for _ in range(k+1):
            temp = dist.copy()
            for s, d, p in flights:
                if dist[s] == math.inf:
                    continue 
                if dist[s] + p < temp[d]:
                    temp[d] = dist[s] + p
            dist = temp

        return dist[dst] if dist[dst] < math.inf else -1
