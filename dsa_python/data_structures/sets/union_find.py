class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n)) # V = 5 -> parent = [0, 1, 2, 3, 4] -> {0}, {1}, {2}, {3}, {4}
        self.rank = [0] * n
        self.size = [1] * n
        
    def find(self, i: int) -> int:
        # Base case
        if self.parent[i] == i:
            return i
        
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union_by_rank(self, i: int, j: int) -> None:
        i_root = self.find(i)
        j_root = self.find(j)
        
        # Belong to same set
        if i_root == j_root: return
         
        if self.rank[i_root] < self.rank[j_root]:
            self.parent[i_root] = j_root
        elif self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i_root
        else:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1   
    
    def union_by_size(self, i: int, j: int) -> None:
        i_root = self.find(i)
        j_root = self.find(j)
        
        if i_root == j_root: return
        
        i_size = self.size[i_root]
        j_size = self.size[j_root]
        
        if i_size < j_size:
            self.parent[i_root] = j_root
            self.size[j_root] += self.size[i_root]
        elif i_size > j_size:
            self.parent[j_root] = i_root
            self.size[i_root] += self.size[j_root]
        else:
            self.parent[j_root] = i_root
            self.size[i_root] += self.size[j_root]
            
        
if __name__ == '__main__':
    n = 5
    uf = UnionFind(n)
    uf.union_by_rank(0, 1)
    uf.union_by_rank(2, 3)
    uf.union_by_rank(0, 4)
    
    for i in range(n):
        print(f'Element: {i}: Root: {uf.find(i)}')