class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    if root == None:
        return []
    inorder = []
    st = []
    node = root
    while True:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            if not st:
                break
            node = st.pop()
            inorder.append(node.data)
            node = node.right
    return inorder

