import class_level_wise_trasversal


def check_bst(root):
    if root==None:return True,-100000,100000
    left=check_bst(root.left)
    right=check_bst(root.right)

    if left[1]>root.data and right[2]<=root.data:
        result=False
    else:
        result=True
    maxi=max(root.data,left[1],right[1])
    mini=min(root.data,left[2],left[2])

    isbst=result and left[0] and right[0]
    return isbst ,maxi,mini


bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
bst.print_tree_levelwise(root)
print(check_bst(root)[0])
