class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def main(root, val):
    if root is None:
        return None
    if root.val == val:
        return delete_node_iterative(root)
    parent = None
    curr = root
    while curr and curr.val!=val:
        parent = curr
        if val<curr.val:
            curr = curr.left
        else:
            curr = curr.right
    if curr is None:
        return root
    if curr.left is None and curr.right is None:
        if parent.left == curr:
            parent.left = None
        else:
            parent.right = None
        return root
    if curr.left is None or curr.right is None:
        child = curr.left if curr.left else curr.right
        if parent.left == child:
            parent.left = child
        else:
            parent.right = child
        return root
    successor_parent = curr
    successor = curr.right
    while successor.left:
        successor_parent = successor
        successor = successor.left
    curr.left = successor.val
    if successor_parent== curr:
        curr.right = successor.right
    else:
        successor_parent.left = successor.right
    return root
def delete_node_iterative(root):
    """
    Special function to delete root node.
    
    Root has no parent, so needs different handling.
    
    Args:
        root: The root node to delete
    
    Returns:
        New root node
    """
    # CASE 1: Root is leaf (tree with only one node)
    if root.left is None and root.right is None:
        return None
    
    # CASE 2: Root has only right child
    if root.left is None:
        return root.right
    
    # CASE 2: Root has only left child
    if root.right is None:
        return root.left
    
    # CASE 3: Root has two children
    # Find successor in right subtree
    successor_parent = root
    successor = root.right
    
    # Go left to find leftmost (smallest)
    while successor.left:
        successor_parent = successor
        successor = successor.left
    
    # Copy successor value to root
    root.val = successor.val
    
    # Delete successor
    if successor_parent == root:
        # Successor is direct right child
        root.right = successor.right
    else:
        # Successor is deeper in tree
        successor_parent.left = successor.right
    
    return root