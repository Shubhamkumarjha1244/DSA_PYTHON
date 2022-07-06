import generate_binary_tree

def Greater_than(root,num):
    if root==None:
        return 0
    left_greater=Greater_than(root.left,num)
    right_greater=Greater_than(root.right,num)
    if root.data>num:
        return left_greater+right_greater+1
    else:
        return left_greater+right_greater

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
num=int(input('Number to compare'))
print(Greater_than(root,num))