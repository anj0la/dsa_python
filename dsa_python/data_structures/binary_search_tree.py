class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def insert(root, val):
    if not root:
        return TreeNode(val)
        
    if root.val == val:
        raise ValueError(f'Value: {val} already exists in the tree.') 
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
        print(root.val, end=' ')
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
    
    left_height = 1 + get_height(root.left)
    right_height = 1 + get_height(root.right)
    
    return max(left_height, right_height)   

def get_min(root):
    if not root.left:
        return root.val
    
    return get_min(root.left)
    
def get_max(root):
    if not root.right:
        return root.val
    
    return get_max(root.right)     

def get_successor(node):
    node = node.right
    while node and node.left:
        node = node.left
        
    return node

def get_predecessor(node):
    node = node.left
    while node and node.right:
        node = node.right
        
def delete(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else: # We are at the node we want to delete
        
        # Case 1 & 2 - When root has 0 children or either only one child (left or right subtree)
        if not root.left:
            return root.right
            
        if not root.right:
            return root.left
            
        # Case 3 - root's left and right children have nodes (i.e., left and right are subtrees)
        succ = get_successor(root)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
        
    return root
        
        
if __name__ == '__main__':
    root = TreeNode(50)
    root = insert(root, 30) 
    root = insert(root, 80)
    root = insert(root, 25)
    root = insert(root, 40)
    root = insert(root, 68)
    root = insert(root, 100)
    root = insert(root, 58)
    root = insert(root, 70)
    
    node_count = get_node_count(root)
    print('Node count: ', node_count)
  
    print_values(root)
    print()
    
    print(is_in_tree(root, 20))
    
    height = get_height(root)
    print('Height of tree: ', height)
    
    min_val = get_min(root)
    print('Minimum value of tree: ', min_val)
    
    max_val = get_max(root)
    print('Maximum value of tree: ', max_val)
    
    root = delete(root, 80)
    print_values(root)
    print()
    
"""     root = delete(root, 25)
    print_values(root)
    print()
    
    root = delete(root, 30)
    print_values(root)
    print()
     """