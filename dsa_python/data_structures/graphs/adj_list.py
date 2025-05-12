class AdjList:
    def __init__(self, V, directed = False):
        self.adj = [[] for _ in range(V)]
        self.directed = directed
        
    def vertices(self) -> list:
        return [i for i in range(len(self.adj))]
    
    def edges(self) -> list:
        return [f'{i} -> {lst}' for i, lst in enumerate(self.adj)]
    
    def vertex_count(self) -> int:
        return len(self.adj)
    
    def edge_count(self) -> int:
        count = total = 0
        for lst in self.adj:
            for _ in lst:
                count += 1
            total += count
            count = 0
            
        return total // 2 if not self.directed else total
        
    def get_edge(self, u, v) -> bool:
        return v in self.adj[u]
    
    def deg(self, v) -> int:
        if not self.directed:   
            return len(self.adj[v])
        else:
            in_deg = sum([1 for lst in self.adj for u in lst if u == v])
            out_deg = len(self.adj[v])
            
            return in_deg + out_deg
    
    def incident(self, u) -> int:
        if not self.directed:
            return len(self.adj[u])
        else:
            in_edges = sum([1 for lst in self.adj for v in lst if v == u])
            out_edges = len(self.adj[u])
            return in_edges + out_edges
    
    def add_edge(self, u, v) -> None:
        # assumes that u and v are valid vertices in the adjacency list
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)
    
    def remove_edge(self, u, v) -> None:
        self.adj[u].remove(v)
        if not self.directed:
            self.adj[v].remove(u)
            
class WeightedAdjList:
    def __init__(self, V = 0, directed = False) -> None:
        self.adj = [[] for _ in range(V)]
        self.directed = directed
        
    def vertices(self) -> list:
        return [i for i in range(len(self.adj))]
    
    def edges(self) -> list:
        return [f'{i} -> {lst}' for i, lst in enumerate(self.adj)]
            
    def vertex_count(self) -> int:
        return len(self.adj)
    
    def edge_count(self) -> int:
        total = sum(len(lst) for lst in self.adj)
        return total // 2 if not self.directed else total
    
    def get_edge(self, u, v) -> int:
        for w, weight in self.adj[u]:
            if w == v:
                return weight    
        return -1    
    
    def deg(self, v) -> int:
        if not self.directed:
            return len(self.adj[v])
        else:
            in_deg = sum([1 for lst in self.adj for u, _ in lst if u == v])
            out_deg = len(self.adj[v])
            
            return in_deg + out_deg
    
    def incident(self, u) -> int:
        if not self.directed:
            return len(self.adj[u])
        else:
            in_edges = sum([1 for lst in self.adj for v, _ in lst if v == u])
            out_edges = len(self.adj[u])
            
            return in_edges + out_edges
    
    def add_edge(self, u, v, w) -> None:
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))   
    
    def remove_edge(self, u, v) -> None:
        self.adj[u] = [pair for pair in self.adj[u] if pair[0] != v]
        if not self.directed:
            self.adj[v] = [pair for pair in self.adj[v] if pair[0] != u]

if __name__ == '__main__':
    graph = WeightedAdjList(4, directed = False)
    graph.add_edge(0, 1, 100)
    graph.add_edge(0, 2, 200)
    graph.add_edge(1, 2, 300)
    graph.add_edge(2, 3, 400)
    
    print(f'Vertices: {graph.vertices()}')
    print(f'Edges: {graph.edges()}')
    print(f'Vertex count: {graph.vertex_count()}')
    print(f'Edge count: {graph.edge_count()}')
    print(f'Value of edge (0, 2): {graph.get_edge(0, 2)}')

    print(f'Degree of vertex 2: {graph.deg(2)}')
    print(f'Incident edges of vertex 2: {graph.incident(2)}')

    graph.remove_edge(0, 2)
    print(f'Edges: {graph.edges()}')
    print(f'Value of edge (0, 2): {graph.get_edge(0, 2)}')
    
   