res = []
def main(root):
    if root is None:
        res.append('N')
        return
    res.append(root.val)
    main(root.left)
    main(root.right)
index = 0
def deserialize(s):
    if s[index] == 'N':
        index+=1
        return None
    val = TreeNode(s[index])
    index+=1
    val.left = deserialize(s)
    val.right = deserialize(s)
    return val