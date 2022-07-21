import class_level_wise_trasversal

def search_btw(root,k1,k2):
    if root==None:return
    
    if root.data>=k1 and root.data<=k2:
        search_btw(root.left,k1,k2)
        print(root.data,end=' ')
        search_btw(root.right,k1,k2)
    elif root.data>k2:
        search_btw(root.left,k1,k2)    
    elif root.data<k1:
        search_btw(root.right,k1,k2)
    
    
bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
bst.print_tree_levelwise(root)
k1=int(input('Enter lower limit : '))
k2=int(input('Enter higher limit : '))
search_btw(root,k1,k2)

    
