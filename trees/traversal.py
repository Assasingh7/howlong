class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def main(root:Node):
    pre_order, in_order, post_order = [], [], []
    st = []
    st.append((root, 1))
    while st:
        node, lvl = st.pop()
        if lvl == 1:
            pre_order.append(node.data)
            st.append((node, 2))
            if node.left:
                st.append((node.left, 1))
        elif lvl == 2:
            in_order.append(node.data)
            st.append((node, 3))
            if node.right:
                st.append((node.right, 1))
        else:
            post_order.append(node.data)
    return pre_order, in_order, post_order

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(main(root))