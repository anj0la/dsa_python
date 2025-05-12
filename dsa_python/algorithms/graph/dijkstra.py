from data_structures.graphs.adj_list import WeightedAdjList
from data_structures.graphs.adj_matrix import WeightedAdjMatrix
import heapq

def dijkstra(graph: WeightedAdjList, source: int) -> dict:
    dist = {node: float('inf') for node in range(graph.vertex_count())}
    dist[source] = 0
    visited = [False] * len(graph.adj)
    
    # Create a priority queue
    priority_queue = [(0, source)]
    heapq.heapify(priority_queue)
    
    while priority_queue: 
        curr_dist, u = heapq.heappop(priority_queue) # extracting the minimum value
        
        if visited[u]:
            continue
        
        visited[u] = True
            
        # Perform relaxation
        for v, weight in graph.adj[u]:
            if curr_dist + weight < dist[v]:
                dist[v] = curr_dist + weight
                heapq.heappush(priority_queue, (dist[v], v))
                    
    return dist

def dijkstra_matrix(graph: WeightedAdjMatrix, source: int) -> dict:
    V = len(graph.matrix)
    dist = {node: float('inf') for node in range(V)}
    dist[source] = 0
    visited = [False] * V
    
    pq = [(0, source)]
    heapq.heapify(pq)
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
            
        for v in range(V):
            if graph.matrix[u][v] > 0 and curr_dist + graph.matrix[u][v] < dist[v]:
                dist[v] = curr_dist + graph.matrix[u][v]
                heapq.heappush(pq, (dist[v], v))
                    
    return dist
       
            
    