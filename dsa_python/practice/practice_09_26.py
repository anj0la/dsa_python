from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val == root.val:
        raise ValueError(f'{val} already exists in the tree.')
    elif val < root.val:
        root.left = insert(root.left, val)
    else: # val > root.val
        root.right = insert(root.right, val)
        
    return root


def get_node_count(root):
    if not root:
        return 0
    return 1 + get_node_count(root.left) + get_node_count(root.right)


def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
        

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)
        
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)
        
def is_in_tree(root, val):
    if not root:
        return False
    
    if val == root.val:
        return True
    elif val < root.val:
        return is_in_tree(root.left, val)
    else: # val > root.val
        return is_in_tree(root.right, val)
    
    
def get_height(root):
    if not root:
        return 0
    
    lh = 1 + get_height(root.left)
    rh = 1 + get_height(root.right)
    
    return max(lh, rh)


def get_min_depth(root):
    if not root:
        return 0
    
    if not root.left:
        return 1 + get_min_depth(root.right)
    
    if not root.right:
        return 1 + get_min_depth(root.left)
    
    lh = 1 + get_min_depth(root.left)
    rh = 1 + get_min_depth(root.right)
    
    return min(lh, rh)

def get_max(root):
    if not root.right:
        return root
    
    return get_max(root.right)

def get_min(root):
    if not root.left:
        return root
    
    return get_min(root.left)

def is_binary_search_tree(root):
    
    def valid(root, min, max):
        if not root:
            return True
        
        if not(min < root.val < max):
            return False
        
        return valid(root.left, min, root.val) + valid(root.right, root.val, max)
    
    return valid(root, float('-inf'), float('inf'))

def get_successor(node):
    node = node.right
    while node and node.left:
        node = node.left
        
    return node

def get_predecessor(node):
    node = node.left
    while node and node.right:
        node = node.right
        
    return node

def delete(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Case 1 and 2
        if not root.right:
            return root.left
        
        if not root.left:
            return root.right
        
        # Case 3
        succ = get_successor(root)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
        
    return root

def inorder_successor(root, val):
    if not root:
        return None
    
    succ = TreeNode()
    
    while root:
        if val == root.val and root.right:
            return get_successor(root)
        elif root.val > val:
            succ = root
            root = root.left
        else:
            root = root.right
            
    return succ


def inorder_predecessor(root, val):
    if not root:
        return None
    
    prec = TreeNode()
    
    while root:
        if val == root.val and root.left:
            return get_predecessor(root)
        elif root.val < val:
            prec = root
            root = root.right
        else:
            root = root.left
            
    return prec


def is_symmetric(root1, root2):
    
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    return is_mirror(root1.left, root2.right)


def level_order_traversal(root): # BFS
    if root:
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            print(node.val)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                

def print_tree_in_level_order(root):
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
    
    