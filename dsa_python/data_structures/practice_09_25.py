class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None
        
        
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val == root.val:
        raise ValueError('Cannot have duplicate values in a BST.')
    elif val < root.val:
        root.left = insert(root.left, val)
    else: # val > root.val
        root.right = insert(root.right, val)
        
    return root

def get_node_count(root):
    if not root:
        return 0
    return 1 + get_node_count(root.left) + get_node_count(root.right)

def print_values(root):
    if root:
        print_values(root.left)
        print(root.val, end= ' ')
        print_values(root.right)
        
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
        if not root.right:
            return root.left
        
        if not root.left:
            return root.right
        
        # Case 3
        succ = get_successor(root)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
        
    return root
    
def get_inorder_successor(root, val):
    succ = TreeNode(None)
    
    while root:
        if root.right and root.val == val:
            return get_successor(root)
        if root.val < val:
            root = root.right
        if root.val > val:
            succ = root
            root = root.left
            
    return succ

def get_inorder_predecessor(root, val):
    pre = TreeNode(None)
    
    while root:
        if root.left and root.val == val:
            return get_predecessor(root)
        if root.val < val:
            pre = root
            root = root.right
        if root.val > val:
            root = root.left
            
    return pre
    