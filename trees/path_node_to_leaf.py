def main(root, x, res):
    if root is None:
        return False
    res.append(root.data)
    if root.val==x:
        return True
    if main(root.left, x, res) or main(root.right, x, res):
        return True
    res.pop()
    return False