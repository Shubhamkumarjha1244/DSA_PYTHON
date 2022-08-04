from turtle import right
import class_level_wise_trasversal




def bt_to_linklist(root):      #using stack
    if root==None:return 
    st=[]
    st.append(root)
    while len(st)!=0:
        node=st.pop()
        if node.right:st.append(node.right)
        if node.left:st.append(node.left)
        if len(st)>1:node.right=st[-1]
        else:node.right=None
        node.left=None
    return root



bt=class_level_wise_trasversal.level_wise_trans()
root=bt.input_level_wise()
bt.print_tree_levelwise(root)
root=bt_to_linklist(root)
bt.print_tree_levelwise(root)