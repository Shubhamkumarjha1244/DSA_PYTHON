import queue
import class_level_wise_trasversal

def zig_zag_transversal(root):
    if not root:return
    qu=queue.Queue()
    qu.put([root])
    zig_zag=[[root.data]]
    left=False
    while not qu.empty():
        level=qu.get()
        new_level=[]
        for node in level:
            if node.left:new_level.append(node.left)
            if node.right:new_level.append(node.right)
        if len(new_level)==0:break
        else:
            if left==True:
                qu.put(new_level)
                zig_zag.append([ele.data for ele in new_level])
            else:
                new_level_rev=new_level[::-1]
                qu.put(new_level)
                zig_zag.append([ele.data for ele in new_level_rev])
            left=not(left)
    return zig_zag

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print('------------------------')
print(zig_zag_transversal(root))
        