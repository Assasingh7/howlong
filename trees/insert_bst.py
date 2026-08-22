def main(root, val):
    if not root:
        return None
    curr=root
    while True:
        if val<curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
        elif val>curr.val:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right
        else:
            break
    return root
