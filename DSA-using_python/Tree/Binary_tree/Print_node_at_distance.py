
import class_level_wise_trasversal
def find_node_depth(root,node_val,depth=0):
    if root==None:
        return None,0
    if root.data==node_val:
        return root,depth
    dep_left=find_node_depth(root.left,node_val,depth+1)
    dep_right=find_node_depth(root.right,node_val,depth+1)
    return dep_left[0] or dep_right[0],dep_left[1] or dep_right[1]

def Print_nodes(root,given,node_val,depth=0):
    if root==None:return 
    if depth==given and root.data!=node_val:
        print(root.data)
    Print_nodes(root.left,given,node_val,depth+1)
    Print_nodes(root.right,given,node_val,depth+1)

def Print_node_at_distance(root,node_val,distance):
    node=find_node_depth(root,node_val)[0]
    if not node:return -1
    depth=find_node_depth(root,node_val)[1]
    if depth<=distance:
        different_node_depth=distance-depth
        if different_node_depth==0:print(root.data,end='')
        else:
            Print_nodes(root,different_node_depth,node_val)
    Print_nodes(node,distance,node_val)



tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
node_value=int(input('Enter node value'))
distance=int(input('Enter distance'))
print('--------------')
Print_node_at_distance(root,node_value,distance)



