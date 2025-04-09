class BinaryTree:
    def __init__(self) -> None:
        self.tree = []
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def left(self, i: int) -> int:
        return (2 * i) + 1
    
    def right(self, i: int) -> int:
        return (2 * i) + 2
    
    def insert(self, val: int):
        self.tree.append(val)
        
    def pre_order_traversal(self, i=0):
        if i >= len(self.tree):
            return []
        return [self.tree[i]] + self.pre_order_traversal(self.left(i)) + self.pre_order_traversal(self.right(i))
    
    def in_order_traversal(self, i=0):
        if i >= len(self.tree):
            return []
        return self.in_order_traversal(self.left(i)) + [self.tree[i]] + self.in_order_traversal(self.right(i))
    
    def post_order_traversal(self, i=0):
        if i >= len(self.tree):
            return []
        return self.post_order_traversal(self.left(i)) + self.post_order_traversal(self.right(i)) + [self.tree[i]]
            
if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    print('Preorder Traversal: ', tree.pre_order_traversal())
    print('In-order Traversal: ', tree.in_order_traversal())
    print('Postorder Traversal: ', tree.post_order_traversal())