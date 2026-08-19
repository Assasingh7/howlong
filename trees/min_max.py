def main(root):
    if root is None:
        return None, None
    ml = root
    mr = root
    while ml.left:
        ml = ml.left
    while mr.right:
        mr = mr.right
    return ml.data, mr.data
