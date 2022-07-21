import class_level_wise_trasversal


def bst_from_sorted_array(arr):
    if len(arr)==0:return
    mid=len(arr)//2
    root=class_level_wise_trasversal.BinaryTreeNode(arr[mid])
    root.left=bst_from_sorted_array(arr[:mid])
    root.right=bst_from_sorted_array(arr[mid+1:])
    return root

bst=class_level_wise_trasversal.level_wise_trans()
arr=[int(ele) for ele in input().split(' ')]
root=bst_from_sorted_array(arr)
bst.print_tree_levelwise(root)
