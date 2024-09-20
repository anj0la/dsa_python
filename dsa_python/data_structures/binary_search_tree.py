class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val == root.val: # No duplicate elements
        return root
    if val < root.val:
        root.left = insert(root.left, val)
    else:
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
    else:
        return is_in_tree(root.right, val)
    
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