class EdgeList:
    def __init__(self, is_directed = False) -> None:
        self.edge_list = []
        self.directed = is_directed
        
    def vertices(self) -> list:
        vertices = set() # A set inherently does not allow duplicates
        for edge in self.edge_list:
            u, v = edge
            vertices.add(u)
            vertices.add(v)
            
        return list(vertices)
    
    def edges(self) -> list:
        edges = []
        for edge in self.edge_list:
            u, v = edge
            edges.append(f'{u}-{v}')
            
        return edges
    
    def vertex_count(self) -> int:
        vertices = set()
        for edge in self.edge_list:
            u, v = edge
            vertices.add(u)
            vertices.add(v)
            
        return len(vertices)
    
    def edge_count(self) -> int:
        return len(self.edge_list)
    
    def get_edge(self, u, v) -> bool:
        for edge in self.edge_list:
            x, y = edge
            
            # Undirected, check if (u, v) or (v, u) exists
            if not self.directed:
                if (x == u and y == v) or x == v and y == u:
                    return True
                
            # Directed, check if (u, v) exists
            else:
                if x == u and y == v:
                    return True
            
        return False
    
    def deg(self, v) -> int:
        # Undirected - count # of adj vertices (avoiding duplicates)
        if not self.directed:
            adj = set()
            for edge in self.edge_list:
                u, w = edge
                if u == v:
                    adj.add(w)
                if w == v:
                    adj.add(u)
        
            return len(adj)
        
        # Directed - count # of incoming (in degree) and outgoing (out degree) vertices
        else:
            in_deg = out_deg = 0
            for edge in self.edge_list:
                u, w = edge
                if w == v:
                    in_deg += 1
                if u == v:
                    out_deg += 1
            
            return in_deg + out_deg
    
    def incident(self, u) -> int:
        if not self.directed:
            inc = set()
            for edge in self.edge_list:
                v, w = edge
                if v == u:
                    inc.add(w)
                if w == u:
                    inc.add(v)
                    
            return len(inc)
        else:
            in_edge = out_edge = 0
            for edge in self.edge_list:
                v, w = edge
                # Get the count of the incoming edge - (v, w) where v -> w
                if w == u:
                    in_edge += 1
                # Get the count of the outgoing edge - (w, v) where w -> v
                if v == u:
                    out_edge += 1
                    
            return in_edge + out_edge
                    
    
    def add_edge(self, u, v) -> None:
        self.edge_list.append((u, v))
        if not self.directed:
            self.edge_list.append((v, u))

    def remove_edge(self, u, v) -> None:
        count = 0
        for i, edge in enumerate(self.edge_list):
            x, y = edge
                
            if x == u and y == v:
                self.edge_list[i], self.edge_list[-1] = self.edge_list[-1], self.edge_list[i]
                self.edge_list.pop()
                count += 1
            
            if not self.directed:
                if x == v and y == u:
                    self.edge_list[i], self.edge_list[-1] = self.edge_list[-1], self.edge_list[i]
                    self.edge_list.pop()
                    count += 1
                    
            if not self.directed:
                if count >= 2:
                    break
            else:
                if count >= 1:
                    break
                
class WeightedEdgeList:
    def __init__(self, is_directed = False) -> None:
        self.edge_list = []
        self.directed = is_directed
        
    def vertices(self) -> list:
        vertices = set()
        for edge in self.edge_list:
            u, v, _ = edge
            vertices.add(u)
            vertices.add(v)
            
        return list(vertices)
    
    def edges(self) -> list:
        edges = []
        for edge in self.edge_list:
            u, v, w = edge
            edges.append(f'{u}->{v} with weight: {w}')
            
        return edges
    
    def vertex_count(self) -> int:
        vertices = set()
        for edge in self.edge_list:
            u, v, _ = edge
            vertices.add(u)
            vertices.add(v)
            
        return len(vertices)
    
    def edge_count(self) -> int:
        return len(self.edge_list)
    
    def get_edge(self, u, v) -> int:
        for edge in self.edge_list:
            x, y, w = edge
            if not self.directed:
                if (x == u and y == v) or (x == v and y == u):
                    return w    
            else:
                if x == u and y == v:
                    return w
                
        return -1 # no edge exists
    
    def deg(self, v) -> int:
        if not self.directed:
            adj = set()
            for edge in self.edge_list:
                x, y, _ = edge
                if x == v:
                    adj.add(y)
                if y == v:
                    adj.add(x)
                    
            return len(adj)
        
        else:
            in_deg = out_deg = 0
            for edge in self.edge_list:
                x, y, _ = edge
                if x == v:
                    out_deg += 1
                if y == v:
                    in_deg += 1
                    
            return in_deg + out_deg
                    
    def incident(self, u) -> int:
        if not self.directed:
            inc = set()
            for edge in self.edge_list:
                x, y, _ = edge
                if x == u:
                    inc.add(y)
                if y == u:
                    inc.add(x) 
            
            return len(inc)
            
        else:
            in_inc = out_inc = 0
            for edge in self.edge_list:
                x, y, _ = edge
                if x == u:
                    out_inc += 1
                if y == u:
                    in_inc += 1
            
            return in_inc + out_inc
            
    def add_edge(self, u, v, w) -> None:
        self.edge_list.append((u, v, w))
        if not self.directed:
            self.edge_list.append((v, u, w))

    def remove_edge(self, u, v) -> None:
        count = 0
        for i, edge in enumerate(self.edge_list):
            x, y, _ = edge
                
            if x == u and y == v:
                self.edge_list[i], self.edge_list[-1] = self.edge_list[-1], self.edge_list[i]
                self.edge_list.pop()
                count += 1
            
            if not self.directed:
                if x == v and y == u:
                    self.edge_list[i], self.edge_list[-1] = self.edge_list[-1], self.edge_list[i]
                    self.edge_list.pop()
                    count += 1
                    
            if not self.directed:
                if count >= 2:
                    break
            else:
                if count >= 1:
                    break
                              
if __name__ == '__main__':
    graph = WeightedEdgeList()
    graph.add_edge(1, 2, 100)
    graph.add_edge(1, 3, 300)
    print(f'Vertices: {graph.vertices()}')
    print(f'Edges: {graph.edges()}')
    print(graph.get_edge(1, 4)) # -1
    graph.remove_edge(1, 2)
    print(f'Vertices: {graph.vertices()}')
    print(f'Edges: {graph.edges()}')
    
# edge_list = [(1, 2), (1, 3), (2, 3)]
# edge_list = [('A', 'B'), ('A', 'G'), ('G', 'F'), ('F', 'B'), ('B', 'C'), ('C', 'F'), ('F', 'E'), ('E', 'C'), ('C', 'D')]        
