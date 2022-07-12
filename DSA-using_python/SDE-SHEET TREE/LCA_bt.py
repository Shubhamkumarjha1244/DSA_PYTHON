import class_level_wise_trasversal

def LCA_bt(root,p,q):
    if root==None or root.data==p or root.data==q:
        return root
    
    left=LCA_bt(root.left,p,q)
    right=LCA_bt(root.right,p,q)

    if left==None:return right
    elif right==None:return left
    elif left and right:
        return root


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
p=int(input('enter first node'))
q=int(input('enter second node'))
ans=LCA_bt(root,p,q)
print(ans.data)