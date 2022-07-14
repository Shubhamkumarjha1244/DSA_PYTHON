import class_level_wise_trasversal

def max_sum_BT(root):
    if root==None:return 0,0
    left=max_sum_BT(root.left)
    right=max_sum_BT(root.right)
    node_sum=root.data+max(left[0],right[0])
    max_sum=max((node_sum+min(left[0],right[0])),left[1],right[1])
    return node_sum,max_sum






tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print(max_sum_BT(root)[1])
