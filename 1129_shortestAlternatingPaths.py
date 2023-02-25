class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1 for _ in range(n)]
        count = 0
        
        graph = [[] for _ in range(n)]
        for src, dst in redEdges:
            graph[src].append((dst, "red"))
        for src, dst in blueEdges:
            graph[src].append((dst, "blue"))
        
        visited = collections.deque([(0, "first")])
        while visited:
            for _ in range(len(visited)):
                # visit node and get color of edge to that node 
                prevNode, prevColor = visited.popleft()
                if ans[prevNode] == -1:
                    ans[prevNode] = count
                # look at each node that this node connects to
                for i, (curNode, curColor) in enumerate(graph[prevNode]):
                    if curColor != prevColor and curNode != -1:
                        visited.append((curNode, curColor))
                        graph[prevNode][i] = (-1, curColor)
            count += 1

        return ans 
