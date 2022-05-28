class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Linked list implementation of queue, because constant time deletion at front and insertion at back
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, val):
        new = ListNode(val)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = self.tail.next
    
    def pop(self):
        self.head = self.head.next
    
    def read(self):
        return self.head.data
    
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
    
class Graph:
    vertices = {}   # Hash table storing all nodes in graph (node value : actual node)
    def __init__(self, data=None):
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
    
    def DFS(self, val, visited={}):
        visited[self.data] = True
    
        if self.data == val:
            return "Found " + self.data
        else:
            for vertex in self.adj:
                if visited.get(vertex.data) != None:
                    continue
                else:
                    found = vertex.DFS(val, visited)
                    if found == None:
                        continue
                    else:
                        return found
    
    def BFS(self, val, Q=Queue(), visited={}):
        Q.add(self)
        visited[self.data] = True
        while Q.empty() == False:
            new = Q.read()
            Q.pop()
            if new.data == val:
                return "Found " + new.data
            else:
                for vertex in new.adj:
                    if visited.get(vertex.data) == None:
                        Q.add(vertex)
                        visited[vertex.data] = True
        return "Not Found"
    
    
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
print(Graph.vertices['c'].BFS('h'))