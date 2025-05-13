from data_structures.graphs.adj_matrix import WeightedAdjMatrix
from data_structures.graphs.edge_list import WeightedEdgeList

def bellman_ford(graph: WeightedEdgeList, source: int) -> list:
    # 1. Initialization
    V = len(graph.edge_list)
    dist = [float('inf')] * V
    dist[source] = 0
    
    # 2. Relax all edges V - 1 times
    for _ in range(V):
        for u, v, w in graph.edge_list:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # 3. Check for negative-weight cycles
    for u, v, w in graph.edge_lst:
        if dist[u] + w < dist[v]:
            return # detected a negative-weight cycle
    
    return dist

def bellman_ford_matrx(graph: WeightedAdjMatrix, source: int) -> dict:
    # 1. Initialization
    V = len(graph.matrix)
    dist = {node: float('inf') for node in range(V)}
    dist[source] = 0
    
    # 2. Relax all edges V - 1 times
    for _ in range(V):
        for u in range(V):
            for v in range(V):
                if graph.matrix[u][v] != float('inf'):
                    if dist[u] + graph.matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + graph.matrix[u][v]
                        
    # 3. Check for negative-weight cycles
    for u in range(V):
        for v in range(V):
            if graph.matrix[u][v] != float('inf'):
                if dist[u] + graph.matrix[u][v] < dist[v]:
                        return
                    
    return dist