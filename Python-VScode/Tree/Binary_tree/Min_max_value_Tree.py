import class_level_wise_trasversal

def min_max(root):
    if not root:
        return (10**5)+1,0
    left_sub=min_max(root.left)
    right_sub=min_max(root.right)
    mini=min(root.data,left_sub[0],right_sub[0])
    maxi=max(root.data,right_sub[1],left_sub[1])
    return mini,maxi


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print(min_max(root))