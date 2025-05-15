from data_structures.graphs.edge_list import WeightedEdgeList
from data_structures.sets.union_find import UnionFind

def kruskal(graph: WeightedEdgeList, n: int) -> int:
    # 1. Initialization
    graph.edge_list.sort(key=lambda item: item[2])
    uf = UnionFind(n)
    cost = 0
    count = 0
    
    # 2. Run Kruskal's Algorithm (similar to Cycle Detection)
    for u, v, wt in graph.edge_list:
        
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            cost += wt
            count += 1
            
        if count == n - 1:
            break
        
    return cost
            
    
            