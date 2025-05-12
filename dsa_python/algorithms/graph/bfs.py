from collections import deque
from data_structures.graphs.adj_list import AdjList

def bfs(graph: AdjList, s):
    queue, visited = deque([s]), {s}
    
    while queue:
        v = queue.popleft()
        
        for w in graph.adj[v]:
            if w not in visited:
                queue.append(w)
                visited.add(w)
                
    return visited # the path of visited nodes from the source node s

def bfs_no_ret(graph: AdjList, s):
    queue, visited = deque([s]), [False] * len(graph.adj)
    visited[s] = True
    
    while queue:
        v = queue.popleft()
        
        for w in graph.adj[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
                
    # finished bfs with no ret value
