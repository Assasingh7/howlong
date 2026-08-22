def main(root, target):
    if not root:
        return None
    if root.val == target:
        return target
    if root.val>target:
        return main(root.left, target)
    right_floor = main(root.right, target)
    return right_floor if right_floor else root.val
def main_iter(root, target):
    flr = None
    curr = root
    while curr:
        if curr.val==target:
            return target
        elif curr.val<target:
            flr = curr.val
            curr = curr.right
        else:
            curr = curr.left
    return flr
