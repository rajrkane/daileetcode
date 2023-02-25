class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Time:   O(n)
        Space:  O(log(n)) to O(n)
        """
        adj = collections.defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(src: int, par: int) -> int:
            time = 0
            for dst in adj[src]:
                if dst != par:
                    childTime = dfs(dst, src)
                    if childTime > 0 or hasApple[dst]:
                        time += 2 + childTime 

            return time 

        return dfs(0, -1) 
