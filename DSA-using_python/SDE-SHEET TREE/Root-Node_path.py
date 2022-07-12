import class_level_wise_trasversal

def Root_Node_path(root,node_val,ans):
    if not root:return 
    if node_val==root.data:
        ans=ans+[root.data]
        return ans
    return Root_Node_path(root.left,node_val,ans+[root.data]) or Root_Node_path(root.right,node_val,ans+[root.data])

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
node_val=int(input('Enter node to search-'))
print(Root_Node_path(root,node_val,[]))

