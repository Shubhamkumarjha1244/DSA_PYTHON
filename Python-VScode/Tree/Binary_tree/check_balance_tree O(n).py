import generate_binary_tree

def check_balance_tree(root):
    if root==None:
        return 0,True
    List1=check_balance_tree(root.left)
    List2=check_balance_tree(root.right)
    height=1+max(List1[0],List2[0])
    node_balance=bool(abs(List2[0]-List1[0])<2)
    isbal=node_balance and List2[1] and List1[1]  
    return height,isbal

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print(check_balance_tree(root))



