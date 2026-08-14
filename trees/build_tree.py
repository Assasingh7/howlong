preorder = [1, 2, 4, 5, 3]
inorder  = [4, 2, 5, 1, 3]
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
mapp = {}
for i in range(len(inorder)):
    mapp[inorder[i]]= i
def main(prestrt, instart, inend):
    if instart>inend:
        return None
    pre_root = preorder[prestrt]
    root = TreeNode(pre_root)
    left_size= mapp[pre_root]-instart
    root.left = main(prestrt+1, instart, mapp[pre_root]-1 )    
    root.right = main(prestrt+left_size+1, mapp[pre_root]+1, inend)
    return root    

