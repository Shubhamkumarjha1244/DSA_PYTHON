import generate_binary_tree

def diameter_height_tree(root):
    if root==None:
        return 0,0
    height_left=diameter_height_tree(root.left)[0]
    height_right=diameter_height_tree(root.right)[0]
    sum=height_left+height_right+1
    diameter=max(sum,diameter_height_tree(root.left)[1],diameter_height_tree(root.right)[1])
    height=1+max(height_left,height_right)
    return height,diameter

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print(diameter_height_tree(root))


