from data_structures.graphs.adj_list import WeightedAdjList
from data_structures.graphs.adj_matrix import WeightedAdjMatrix
import heapq

def dijkstra(graph: WeightedAdjList, source: int) -> list:
    # 1. Initialization
    dist = [float('inf')] * len(graph.adj)
    dist[source] = 0
    visited = [False] * len(graph.adj)
    
    # 2. Create a priority queue
    priority_queue = [(0, source)]
    heapq.heapify(priority_queue)
    
    # 3. Relax each edge ONCE
    while priority_queue: 
        curr_dist, u = heapq.heappop(priority_queue) # extracting the minimum value
        
        # Skip if visited
        if visited[u]:
            continue
        
        visited[u] = True
            
        # 4. Perform relaxation ONCE
        for v, weight in graph.adj[u]:
            if curr_dist + weight < dist[v]:
                dist[v] = curr_dist + weight
                heapq.heappush(priority_queue, (dist[v], v))
                    
    return dist

def dijkstra_matrix(graph: WeightedAdjMatrix, source: int) -> dict:
    # 1. Initialization
    V = len(graph.matrix)
    dist = {node: float('inf') for node in range(V)}
    dist[source] = 0
    visited = [False] * V
    
    # 2. Create a priority queue
    pq = [(0, source)]
    heapq.heapify(pq)
    
    # 3. Relax each edge ONCE
    while pq:
        curr_dist, u = heapq.heappop(pq)
       
        # Skip if visited 
        if visited[u]:
            continue
        
        visited[u] = True
        
        # 4. Perform relaxation ONCE  
        for v in range(V):
            if graph.matrix[u][v] > 0 and curr_dist + graph.matrix[u][v] < dist[v]:
                dist[v] = curr_dist + graph.matrix[u][v]
                heapq.heappush(pq, (dist[v], v))
                    
    return dist
       
def all_pairs_dijkstra(graph: WeightedAdjList):
    # 1. Initialization
    V = len(graph.adj)
    result = [[] for _ in range(V)]
    
    # 2. Call Dijkstra's Algorithm for each vertex
    for u in range(V):
        dist = dijkstra(graph, u)
        result[u] = dist
                
    return result
            
    