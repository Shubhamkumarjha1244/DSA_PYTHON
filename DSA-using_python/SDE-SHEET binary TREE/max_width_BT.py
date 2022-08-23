import queue
import class_level_wise_trasversal


def max_width(root):
    if root==None:return 0
    qu=queue.Queue()
    qu.put([[root,0]])
    max_width=1
    while qu.empty()==False:
        level=qu.get()
        next_level=[]
        for ele in level:
            node=ele[0]
            index=ele[1]
            if node.left:
                next_level.append([node.left,(2*index)+1])
            if node.right:
                next_level.append([node.right,(2*index)+2])
        if len(next_level)==0:break
        level_width=((next_level[-1][1]-next_level[0][1])+1)
        max_width=max(max_width,level_width) #vvi
        qu.put(next_level)
    return max_width
    

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print('maximum width')
print(max_width(root))

            

