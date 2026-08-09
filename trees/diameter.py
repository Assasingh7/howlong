def main(root, diameter):
    if root is None:
        return 0
    left = main(root.left, diameter)
    right = main(root.right, diameter)
    diameter = max(diameter, left+ right)
    return 1+max(left, right)
