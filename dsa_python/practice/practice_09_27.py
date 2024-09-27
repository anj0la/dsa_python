from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val == root:
        raise ValueError('f{val} already exists in the tree.')
    elif val < root.val:
        root.left = insert(root.left, val)
    else: # val > root.val
        root.right = insert(root.right)
        
    return root

def get_node_count(root, val):
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

def get_min(root):
    if not root.left:
        return root.val
    return get_min(root.left)

def get_max(root):
    if not root.right:
        return root.val
    return get_max(root.right)

def is_binary_search_tree(root):
    
    def valid(root, min, max):
        if not root:
            return True
        
        if not (min < root.val < max):
            return False
        
        return valid(root.left, min, root.val) and valid(root.right, root.val, max)
    
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
        if not root.left:
            return root.right
        
        if not root.right:
            return root.left
        
        # Case 3
        succ = get_successor(root)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
        
    return root

def inorder_successor(root, val):
    succ = TreeNode()
    
    while root:
        if val == root.val and root.right:
            return get_successor(root)
        elif root.val > val:
            succ = root
            root = root.left
        elif root.val < val:
            root = root.right
        else:
            break
        
    return succ

def inorder_predecessor(root, val):
    prec = TreeNode()
    
    while root:
        if val == root.val and root.left:
            return get_predecessor(root)
        elif root.val < val:
            prec = root
            root = root.right
        elif root.val > val:
            root = root.left
        else:
            break
        
    return prec

def is_symmetric(root1, root2):
    
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    return is_mirror(root1.left, root2.right)


def levelorder_traversal(root):
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
                
                
def print_levels(root):
    queue, res = deque([root]), []
    
    while queue:
        curr_level, level_size = [], len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            curr_level.append(node)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
        res.append(curr_level)
        
    return res        
        