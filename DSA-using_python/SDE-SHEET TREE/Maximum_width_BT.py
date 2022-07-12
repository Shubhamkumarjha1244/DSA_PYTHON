import queue
import class_level_wise_trasversal

def max_width(root):
    if not root:return 0
    width=0
    qu=queue.Queue()
    qu.put(root,None)
    while not qu.empty():
        node=qu.get()
        if node==None and qu.not_empty():
            width=max(width,qu.qsize())
            qu.put(None)
        else:
            if node.left:qu.put(node.left)
            qu.put(node.right)
    return width


