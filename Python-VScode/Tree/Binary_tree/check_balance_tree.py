import generate_binary_tree
# balance tree means height difference at any node should not be greater than 1
def height(root):
    if root==None:
       return 0
    return 1+max(height(root.left),height(root.right))

def isbalance(root):
    if root==None:
        return True
    height_left=height(root.left)
    height_right=height(root.right)
    if abs(height_left-height_right)>1:
        return False
    return isbalance(root.left) and isbalance(root.right)

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print("tree is balance--",isbalance(root))