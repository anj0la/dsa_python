class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        # Insert using BFS (Level order search) - where we use a queue to keep track of the nodes we have visisted
          
    def pre_order_traversal(self):
        if self.root:
            print(self.root.val)
            self.pre_order_traversal(self.root.left)
            self.pre_order_traversal(self.root.right)
            
    def in_order_traversal(self):
        if self.root:
            self.in_order_traversal(self.root.left)
            print(self.root.val)
            self.in_order_traversal(self.root.right)
            
    def post_order_traversal(self):
        if self.root:
            self.post_order_traversal(self.root.left)
            self.post_order_traversal(self.root.right)
            print(self.root.val)
    