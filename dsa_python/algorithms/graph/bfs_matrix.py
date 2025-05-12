from collections import deque
from data_structures.graphs.adj_matrix import AdjMatrix

def bfs(graph: AdjMatrix, s):
    V = len(graph.matrix)
    queue = deque([s])
    visited = [True if i == s else False for i in range(V)]
    
    while queue:
        u = queue.popleft()
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                queue.append(v)
                
def bfs_path(graph: AdjMatrix, s):
    V = len(graph.matrix)
    queue = deque([s])
    path = {s}
    
    while queue:
        u = queue.popleft()
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and v not in path:
                path.add(v)
                queue.append(v)
                
    return path