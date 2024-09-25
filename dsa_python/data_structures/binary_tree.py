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
          
    def pre_order_traversal(self, root):
        if root:
            print(self.root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
            
    def in_order_traversal(self, root):
        if self.root:
            self.in_order_traversal(root.left)
            print(self.root.val)
            self.in_order_traversal(root.right)
            
    def post_order_traversal(self, root):
        if self.root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(self.root.val)
    
    def level_order_traversal(self, root):
        if root:
            queue = []
            queue.append(root)
            
            while queue:
                node = queue.pop(0)
                print(node.val, end=' ')
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        
tree = BinaryTree()
tree.root = TreeNode(50)
tree.root.left = TreeNode(30)
tree.root.right = TreeNode(80)

tree.level_order_traversal(tree.root)
            