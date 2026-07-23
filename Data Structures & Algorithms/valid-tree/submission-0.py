#valid tree conditions
#a node cannot be a child of two different nodes (no cycles)
#must have n-1 edges
#must be fully connected

#DFS
#return false if cyclic or separated (adjacency list, i.e. list of neighbors)
#return true if all nodes visited and no cycle detected

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        
        prev = -1
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit: #alr in visit set, loop present
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n

            
