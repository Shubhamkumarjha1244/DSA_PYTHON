import class_level_wise_trasversal

def LCA(root,p,q):
    if root==None or root.data==p or root.data==q:
            return root
    elif root.data>p.data and root.data>q.data:
        return LCA(root.left,p,q)
    elif root.data<q.data and root.data<p.data:
        return LCA(root.right,p,q)
    else:
        return root

bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
p=int(input('Enter value of p'))
q=int(input('Enter value of q'))
print(LCA(root,p,q))
bst.print_tree_levelwise(root)