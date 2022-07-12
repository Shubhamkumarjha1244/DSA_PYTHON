import queue
import class_level_wise_trasversal

def vertical_transversal(root):
    dic={}
    qu=queue.Queue()
    i=0
    qu.put([root,i],None)
    while not qu.empty():
        temp=qu.get()
        if not temp:
            qu.put(None)
        node=temp[0]
        i=temp[1]
        if node:
            if i not in dic.keys():
                dic[i]=[]
                dic[i].append(node.data)
            else:
                dic[i].append(node.data)
            qu.put([node.left,i-1])
            qu.put([node.right,i+1])
    for i in sorted(dic.keys()):
        for ele in dic[i]:
            print(ele,end=' ')
        print()
        

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
print("--------------------")
vertical_transversal(root)