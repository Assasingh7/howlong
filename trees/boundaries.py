def isLeaf(node):
    return node.left is None and node.right is None
def addLeftboundaries(node, res):
    while node:
        if not isLeaf(node):
            res.append(node.val)
        if node.left:
            node = node.left
        else:
            node = node.right
def addRightboundaries(node, right):
    while node:
        if not isLeaf(node):
            right.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
def addLeaves(node, res):
    while node:
        if isLeaf(node):
            res.append(node.val)
        addLeaves(node.left, res)
        addLeaves(node.right, res)
def main(root):
    if root is None:
        return []
    res = [root.val]
    addLeftboundaries(root.left, res)
    addLeaves(root, res)
    right = []
    addRightboundaries(root.right, right)
    res.extend(reversed(right))
    return res