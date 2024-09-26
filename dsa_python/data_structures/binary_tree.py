from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_level_order(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = []
        queue.append(self.root)
        
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = TreeNode(val)
                break
            else:
                queue.append(node.left)
            
            if not node.right:
                node.right = TreeNode(val)
                break
            else:
                queue.append(node.right)
            
        # Insert using BFS (Level order search) - where we use a queue to keep track of the nodes we have visisted
          
    def pre_order_traversal(self, root):
        if root:
            print(root.val, end=' ')
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
            
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.val, end=' ')
            self.in_order_traversal(root.right)
            
    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.val, end=' ')
    
    def level_order_traversal(self, root):
        print('Level Order Traversal:', end=' ')
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
        print()
        
    def print_tree_in_level_order(self, root):
        queue, res = deque([root]), []

        while queue:
            level, size = [], len(queue)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            res.append(level)
        
        return res
    
        
tree = BinaryTree()
tree.insert_level_order(50)
tree.insert_level_order(30)
tree.insert_level_order(80)
tree.insert_level_order(25)
tree.insert_level_order(40)
tree.insert_level_order(65)
tree.insert_level_order(100)
tree.insert_level_order(58)
tree.insert_level_order(70)

tree.level_order_traversal(tree.root)
print(tree.print_tree_in_level_order(tree.root))