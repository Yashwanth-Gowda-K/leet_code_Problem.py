from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        n = len(degree)
        for node in degree:
            if degree[node] == n - 1:
                return node
        return -1
