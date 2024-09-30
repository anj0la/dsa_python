class Graph:
    def __init__(self, V, is_directed=False):
        self.V = V
        self.directed = is_directed
        self.adj = [[0] * V for _ in range(V)]
        
    def vertex_count(self):
        return self.V
    
    def edge_count(self):
        sum = 0
        for u in range(self.V):
            for v in range(self.V):
                if self.adj[u][v] == 1:
                    sum += 1
                    
        return sum
    
    def vertices(self):
        vertices = []
        for i in range(self.V):
            vertices.append(i)
            
        return vertices
    
    def add_edge(self, u, v):
        if not self.directed:
            self.adj[u][v] = 1
            self.adj[v][u] = 1
        else:
            self.adj[u][v] = 1
            
    def remove_edge(self, u, v):
        if not self.directed:
            self.adj[u][v] = 0
            self.adj[v][u] = 0
        else:
            self.adj[u][v] = 0
            
    def print_graph(self):
        for u in range(self.V):
            print('Vertex: ' + str(u), end=' ')
            for v in range(self.V):
                if self.adj[u][v] == 1:
                    print(' -> ' + str(v), end='')
            print()
            
    def bfs(self, s):
        print(f'BFS at Vertex {s}:', end=' ')
        queue, visited = [s], set([s])
        
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            
            for u in range(self.V):
                if self.adj[v][u] == 1 and u not in visited:
                    queue.append(u)
                    visited.add(u)  
        print()
        
    def dfs(self, s):
        print(f'DFS (Stack) at Vertex {s}:', end=' ')
        stack, visited = [s], set([s])
        
        while stack:
            v = stack.pop()
            print(v, end=' ')
            
            for u in range(self.V):
                if self.adj[v][u] == 1 and u not in visited:
                    stack.append(u)
                    visited.add(u)
                    
        print()
        
        
    def dfs_recursive(self, s):
        visited = set()
        print(f'DFS (Recursive) at Vertex {s}:', end=' ')
        
        def dfs(v, visited):
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                
                for u in range(self.V):
                    if self.adj[v][u] == 1:
                        dfs(u, visited)
                        
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