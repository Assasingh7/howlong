class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    if root == None:
        return []
    curr = root
    st = []
    pre = []
    st.append(curr)
    while st:
        node = st.pop()
        pre.append(node.data)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return pre
