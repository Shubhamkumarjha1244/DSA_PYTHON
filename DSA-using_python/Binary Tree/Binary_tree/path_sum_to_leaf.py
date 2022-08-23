import class_level_wise_trasversal

def path_sum_to_leaf(root,k,ans):
    if k<0 or root==None:return
    if root.left==None and root.right==None:
        if k==root.data :
            ans=ans+str(root.data)
            print(ans)
            return
    path_sum_to_leaf(root.left,k-(root.data),ans+str(root.data)+' ')
    path_sum_to_leaf(root.right,k-(root.data),ans+str(root.data)+' ')

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
path_sum_to_leaf(root,int(input("enter k value")),'')