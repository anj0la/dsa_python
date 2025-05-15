import heapq
from data_structures.graphs.adj_list import WeightedAdjList

def prim_mst(graph: WeightedAdjList) -> int:
    # 1. Initialization
    visited = [False] * len(graph.adj)
    cost = 0
    
    # 2. Create priority queue
    pq = []
    heapq.heappush(pq, (0, 0)) # (cost, node)
    
    # 3. Perform Prim's algorithm (similar to Dijkstra but no relaxation)
    while pq:
        wt, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        cost += wt
        
        for v, weight in graph.adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
                
    return cost    

