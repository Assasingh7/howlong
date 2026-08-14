def main(root):
    if not root:
        return True
    if not root.left and root.right:
        return True
    left = root.left if root.left else 0
    right = root.right if root.right else 0
    if root.val != left.val+right.val:
        return False
    return main(root.left) and main(root.right)