# NOTE: adjacency matrix implementation of undirected graph
# Advantage: O(1) access to check, add, and delete any edges in the current graph
# Disadvantage: add, delete vertex is O(N^2), because delete involves shifting, and add
# involves copying the entire matrix into a bigger matrix first
# NOTE: for the above reason, adjacency matrix is not very useful for sparse graphs
# NOTE: Deletion in this implementation is a bit confusing, since notice that index always exist
# (for instance, delete node 1, we will still have node 1 because we still have 1 as index)
# Although node 1 is deleted, but due to the notation and limitation of labelling, it seems it is
# not deleted. This is another reason to NOT use adjacency matrix as graph representation:
# Relabelling occurs when node is deleted, in this case, node 2 becomes node 1 after deletion
class Graph:
    size = 0
    def __init__(self, n) -> None:
        Graph.size = n
        self.matrix = [[0 for i in range(Graph.size)] for j in range(Graph.size)]
    
    def add_edge(self, v1, v2, weight=1):
        self.matrix[v1][v2] = weight
        self.matrix[v2][v1] = weight
        
    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0
    
    def add_vertex(self):
        Graph.size += 1
        new = [[0 for i in range(Graph.size)] for j in range(Graph.size)]
        for row in range(0, len(self.matrix)):
            for col in range(0, len(self.matrix[row])):
                new[row][col] = self.matrix[row][col]
        self.matrix = new
    
    def remove_vertex(self, v):
        self.matrix.pop(v)
        for row in range(0, len(self.matrix)):
            self.matrix[row].pop(v)

g = Graph(5)
print(g.matrix)
g.add_edge(1,2)
g.add_edge(3,4)
print(g.matrix)
g.add_vertex()
print(g.matrix)
g.remove_vertex(1)
print(g.matrix)