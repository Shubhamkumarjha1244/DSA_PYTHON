import class_level_wise_trasversal

def left_view(root,arr,level=0):
    if root==None:return
    if level==len(arr):
        arr.append(root.data)
    left_view(root.left,arr,level+1)
    left_view(root.right,arr,level+1)

def right_view(root,arr,level=0):
    if root==None:return
    if level==len(arr):
        arr.append(root.data)
    right_view(root.right,arr,level+1)
    right_view(root.left,arr,level+1)


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
arr=[]

left_view(root,arr)
print(arr)
arr=[]
right_view(root,arr)
print(arr)

