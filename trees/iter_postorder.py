class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    if root == None:
        return []
    post_order = []
    st1 = []
    st2 = []
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    while st2:
        post_order.append(st2.pop().data)
    return post_order