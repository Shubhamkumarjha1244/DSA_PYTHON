from queue import Queue
import class_level_wise_trasversal


# def bottom_view_BT(root,i,dic):
#     if root==None:return
#     dic[i]=root.data
#     bottom_view_BT(root.left,i-1,dic)
#     bottom_view_BT(root.right,i+1,dic)


def bottom_view_using_queue(root,dic):
    qu=Queue()
    i=0
    qu.put([root,i])
    while not qu.empty():
        temp=qu.get()
        node=temp[0]
        i=temp[1] 
        if node:
            dic[i]=node.data
            qu.put([node.left,i-1])
            qu.put([node.right,i+1])
    for i in sorted(dic.keys()):
        print(dic[i],end=' ')

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
dic={}
# bottom_view_BT(root,0,dic)
bottom_view_using_queue(root,dic)
# print(dic)
