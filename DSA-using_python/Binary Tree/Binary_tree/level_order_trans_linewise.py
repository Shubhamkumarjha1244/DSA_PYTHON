import queue
import class_level_wise_trasversal

def level_trans_linewise(root):
    if not(root):return 
    qu=queue.Queue()
    qu.put(root)
    qu.put(None)
    while not(qu.empty()):
        node=qu.get()
        if not(node):
            print()
            if not(qu.empty()):
                qu.put(None)#har none aane pe naya none insert bhi hoga main turning point of question
        else:
            print(node.data,end=' ')
            if node.left:qu.put(node.left)
            if node.right:qu.put(node.right)
        
tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
print("------------------linewise---------------")
level_trans_linewise(root)
    