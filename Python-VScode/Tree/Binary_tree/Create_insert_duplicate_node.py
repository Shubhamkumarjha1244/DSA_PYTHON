import class_level_wise_trasversal
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def Create_insert_dulicate_node(root):
    if root==None:return
    if root.left==None and root.right==None:
        root.left=Node(root.data)
        return root
    temp=root.left
    root.left=Node(root.data)
    root.left.left=Create_insert_dulicate_node(temp)
    root.right=Create_insert_dulicate_node(root.right)
    return root


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
Create_insert_dulicate_node(root)
tree.print_tree_levelwise(root)



    
