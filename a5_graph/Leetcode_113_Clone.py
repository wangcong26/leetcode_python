
# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Function to build the graph
# def build_graph():
#     edges = [[2, 4], [1, 3], [2, 4], [1, 3]]
#     graph = defaultdict(list)
#
#     # Loop to iterate over every
#     # edge of the graph
#     for edge in edges:
#         a, b = edge[0], edge[1]
#
#         # Creating the graph
#         # as adjacency list
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return  dfs(node) if node else None

if __name__ == '__main__':
    solution = Solution()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    #TODO: How to convert the list of list to node