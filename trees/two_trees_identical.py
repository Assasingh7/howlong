def main(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
            return False
    if root1.val != root2.val:
        return False
    return main(root1.left) and main(root2.right)