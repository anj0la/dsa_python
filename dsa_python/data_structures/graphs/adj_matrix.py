class AdjMatrix:
    def __init__(self, V = 0, directed = False) -> None:
        self.matrix = [[0] * V for _ in range(V)]
        self.directed = directed
        
    def vertices(self) -> list:
        vertices = []
        for i in range(len(self.matrix)):
            vertices.append(i)
            
        return vertices
    
    def edges(self) -> list:
        edges = []
        V = len(self.matrix)
        for i in range(V):
            for j in range(V):
                if self.matrix[i][j] == 1:
                    edges.append(f'{i}->{j}')
                    
        return edges
    
    def get_edge(self, u, v) -> bool:
        return self.matrix[u][v] == 1
    
    def deg(self, v) -> int:
        if not self.directed:
            return sum(self.matrix[v])
        else:
            V = len(self.matrix)
            in_deg = out_deg = 0
            
            # in degree
            for i in range(V):
                if self.matrix[i][v] == 1:
                    in_deg += 1
            
            # out degree
            for j in range(V):
                if self.matrix[v][j] == 1:
                    out_deg += 1
                    
            return in_deg + out_deg             
    
    def incident(self, u) -> int:
        if not self.directed:
            return sum(self.matrix[u])
        else:
            V = len(self.matrix)
            in_edge = sum([1 for i in range(V) if self.matrix[i][u] == 1])
            out_edge = sum([1 for j in range(V) if self.matrix[u][j] == 1])
            
            return in_edge + out_edge
        
    def add_edge(self, u, v) -> None:
        self.matrix[u][v] = 1
        if not self.directed:
            self.matrix[v][u] = 1
            
    def remove_edge(self, u, v) -> None:
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
            
class WeightedAdjMatrix:
    def __init__(self, V = 0, directed = False) -> None:
        self.matrix = [[0] * V for _ in range(V)]
        self.directed = directed
        
        
    def vertices(self) -> list:
        return [i for i in range(len(self.matrix))]
    
    def edges(self) -> list:
        edges = []
        V = len(self.matrix)
        for i in range(V):
            for j in range(V):
                if self.matrix[i][j] > 0:
                    edges.append(f'{i}->{j} with weight: {self.matrix[i][j]}')
                                    
        return edges
    
    def vertex_count(self) -> int:
        return len(self.matrix)
    
    def edge_count(self) -> int:
        count = 0
        V = len(self.matrix)
        for i in range(V):
            for j in range(V):
                if self.matrix[i][j] > 0:
                    count += 1
                    
        return count
    
    def get_edge(self, u, v) -> int:
        return self.matrix[u][v]
    
    def deg(self, v) -> int:
        if not self.directed:
            return sum(self.matrix[v])
        else:
            V = len(self.matrix)
            in_deg = out_deg = 0
            
            for i in range(V):
                if self.matrix[i][v] > 0:
                    in_deg += 1
                    
            for j in range(V):
                if self.matrix[v][j] > 0:
                    out_deg += 1
                    
            return in_deg + out_deg
    
    def incident(self, u) -> int:
        if not self.directed:
            return sum(self.matrix[u])
        else:
            V = len(self.matrix)
            in_edge = sum([1 for i in range(V) if self.matrix[i][u] > 0])
            out_edge = sum([1 for j in range(V) if self.matrix[u][j] > 0])
            
            return in_edge + out_edge   
    
    def add_edge(self, u, v, w) -> None:
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w
    
    def remove_edge(self, u, v) -> None:
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
        
if __name__ == '__main__':
    graph = AdjMatrix(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    
    print(f'Vertices: {graph.vertices()}')
    print(f'Edges: {graph.edges()}')
    
    print(f'Degree of vertex 1: {graph.deg(1)}')
    
    print(f'Edge (1, 2) exists: {graph.get_edge(1, 2)}')
    
    graph.remove_edge(1, 2)

    print(f'Vertices: {graph.vertices()}')
    print(f'Edges: {graph.edges()}')
    print(f'Edge (1, 2) exists: {graph.get_edge(1, 2)}')
    
    
    