def main(root, p, q):
    if root is None or root==p or root == q:
        return root
    left = main(root.left, p, q)
    right = main(root.right, p, q)
    if left is None:
        return right
    if right is None:
        return left
    else:
        return root