def main(root):
    if not root:
        return 0
    count=[0]
    main_inorder(root, count)
    return count[0]
def main_order(root, count):
    if not root:
        return
    count[0]+=1
    main_order(root.left, count)
    main_order(root.right, count)