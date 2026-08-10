def main(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return True
    if left.val != right.val:
        return False
    return main(left.left, right.right) and main(left.right, right.left)
def helper(root):
    if not root:
        return True
    return main(root.left, root.right)
     
    