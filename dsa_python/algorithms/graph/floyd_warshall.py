from data_structures.graphs.adj_matrix import WeightedAdjMatrix

def floyd_warshall(graph: WeightedAdjMatrix):
    # 1. Initialization
    V = len(graph.matrix)
    dist = [[float('inf') for _ in range(V)] for _ in range(V)]
    
    for i in range(V):
        dist[i][i] = 0
        
    # 2. Loop through k, i and j
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
    return dist
        
    