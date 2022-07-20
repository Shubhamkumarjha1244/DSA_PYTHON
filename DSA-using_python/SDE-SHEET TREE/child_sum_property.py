import class_level_wise_trasversal

def child_sum_property(root):
    if root==None:return
    child_sum=0
    if root.left!=None:child_sum+=root.left.data
    if root.right!=None:child_sum+=root.right.data
    if child_sum<root.data:
        if root.left:root.left.data=root.data
        if root.right:root.right.data=root.data
    if child_sum>root.data:
        root.data=child_sum
    child_sum_property(root.left)
    child_sum_property(root.right)
    child_sum=0
    if root.left!=None:child_sum+=root.left.data
    if root.right!=None:child_sum+=root.right.data
    if root.left or root.right:
        root.data=child_sum
    return root
    

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
root=child_sum_property(root)
tree.print_tree_levelwise(root)