import class_level_wise_trasversal
import queue

def top_view_BT(root,dic):
    qu=queue.Queue()
    i=0
    qu.put([root,i])
    while not qu.empty():
        temp=qu.get()
        node=temp[0]
        i=temp[1]
        if node:
            if i not in dic.keys():
                dic[i]=node.data
            qu.put([node.left,i-1])
            qu.put([node.right,i+1])
    for i in sorted(dic.keys()):
        print(dic[i],end=' ')


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
top_view_BT(root,{})
        
