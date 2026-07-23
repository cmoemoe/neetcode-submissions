"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#how many neighbors can exist? many
#input node will always be the first node in the graph and have 1 as val
#iterate through graph, add nodes at each layer to a group

#empty graph
#go to the first node, add it's immediate neighbors to a group, append it to res
#then for each neighbor, add it's immediate nieghbors to a group, append it to res

#base case: if node.neighbors is []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node): #clone node and neighbors recursively
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None

                
