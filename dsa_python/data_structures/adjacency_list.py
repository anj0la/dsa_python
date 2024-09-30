class Graph:
    def __init__(self, V, is_directed=False):
        self.V = V
        self.directed = is_directed
        self.adj = [[] for _ in range(V)]
        
    def vertex_count(self):
        return self.V
    
    def edge_count(self):
        sum = 0
        for i in range(len(self.adj)):
            sum += len(self.adj[i])
            
        return sum
    
    def vertices(self):
        vertices = []
        for i in range(len(self.adj)):
            vertices.append(i)
            
        return vertices
    
    def add_edge(self, u, v):
        if not self.directed:
            self.adj[u].append(v)
            self.adj[v].append(u)
        else:
            self.adj[u].append(v)
            
    def remove_edge(self, u, v):
        for i in range(len(self.adj[u])):
            if self.adj[u][i] == v:
                self.adj[u].pop(i)
                break
        if not self.directed:
            for i in range(len(self.adj[v])):
                if self.adj[v][i] == u:
                    self.adj[v].pop(i)
                    break
            
    def print_graph(self):
        for v in range(self.V):
            print('Vertex: ' + str(v), end=' ')
            
            for x in self.adj[v]:
                print(' -> ' + str(x), end='')
                
            print()
            
    def bfs(self, s):
        print(f'BFS at Vertex {s}:', end=' ')
        queue, visited = [s], set([s])
        
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            
            for w in self.adj[v]:
                if w not in visited:
                    queue.append(w)
                    visited.add(w)    
        print()
        
    def dfs(self, s):
        print(f'DFS (Stack) at Vertex {s}:', end=' ')
        stack, visited = [s], set([s])
        
        while stack:
            v = stack.pop()
            print(v, end=' ')
            
            for w in self.adj[v]: # Reverse the list to get the same result using the stack
                if w not in visited:
                    stack.append(w)
                    visited.add(w)
                    
        print()
        
    
    def dfs_recursive(self, s):
        visited = set()
        print(f'DFS (Recursive) at Vertex {s}:', end=' ')
        
        def dfs(v, visited):
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                
                for w in self.adj[v]:
                    dfs(w, visited)
       
        return dfs(s, visited)
        
        
if __name__ == '__main__':
    V = 5
    graph = Graph(V, is_directed=False)
    print('Trivial Graph (i.e, graph with no edges): ', graph.adj)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)   
    print('Vertex Count: ', graph.vertex_count())
    print('Edge Count: ', graph.edge_count())
    graph.print_graph()
    graph.bfs(0)
    graph.dfs(0)
    graph.dfs_recursive(0)
    print()