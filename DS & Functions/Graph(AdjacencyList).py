# NOTE: adjacency implementation of undirected graph. For undirected, we need to add & remove
# adjacent for both vertices when add_adj & del_adj are called
# NOTE: each node is represented by data, and an array of adjacents
# In this implementation, we use OOP to create nodes, which point to other adjacent nodes
# thus we can access all nodes within the graph. Another method is to use hashtable of
# values with adjacency list

class Graph:
    vertices = {}   # Hash table storing all nodes in graph (node value : actual node)
    def __init__(self, data=None) -> None:
        self.data = data
        self.adj = []
    
    def add_edge(self, v):
        if v in self.adj: return
        self.adj.append(v)
        v.adj.append(self)  # For undirected graph
    
    def del_edge(self, v):
        self.adj.remove(v)
        v.adj.remove(self)  # For undirected graph
        
    def add_vertex(self, data):     # Take in data and add vertex to entire graph
        if Graph.vertices.get(data) == None:
            v = Graph(data)
            Graph.vertices[data] = v
        else:
            raise Exception("Data already in graph")
    
    def node(self, data):   # Get the actual node from graph
        return Graph.vertices[data]
    
    def print_all(self):
        for key in Graph.vertices.keys():
            adj = self.node(key).adj
            tmp = []
            for node in adj:
                tmp.append(node.data)
            print("NODE: " + self.node(key).data + ", ADJACENT: " + str(tmp))
    
arr = ['a','b','c','d','e','f']
g = Graph()
for val in arr:
    g.add_vertex(val)
print(Graph.vertices)

# NOTE: Could make this shorter by writing another help function but I'm too lazy
g.node('a').add_edge(g.node('b'))
g.node('a').add_edge(g.node('c'))
g.node('a').add_edge(g.node('d'))
g.node('b').add_edge(g.node('a'))
g.node('b').add_edge(g.node('c'))
g.node('c').add_edge(g.node('a'))
g.node('c').add_edge(g.node('b'))
g.node('c').add_edge(g.node('e'))
g.node('d').add_edge(g.node('a'))
g.node('d').add_edge(g.node('e'))
g.node('e').add_edge(g.node('d'))
g.node('e').add_edge(g.node('c'))
g.node('e').add_edge(g.node('f'))
g.node('a').add_edge(g.node('e'))
g.add_vertex('g')
g.node('g').add_edge(g.node('c'))
g.node('g').add_edge(g.node('d'))

g.print_all()
            

    