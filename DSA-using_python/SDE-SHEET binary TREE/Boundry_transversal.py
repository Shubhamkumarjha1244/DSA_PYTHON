import class_level_wise_trasversal
def left_view(root,dep,arr):
    if root==None:return
    if dep==len(arr):
        arr.append(root.data)
    left_view(root.left,dep+1,arr)
    left_view(root.right,dep+1,arr)

def right_view(root,dep,arr):
    if root==None:return
    if dep==len(arr):
        arr.append(root.data)
    right_view(root.right,dep+1,arr)
    right_view(root.left,dep+1,arr)

def leaf_view(root,arr):
    if root==None:return
    if root.left==None and root.right==None:
        arr.append(root.data)
    leaf_view(root.left,arr)
    leaf_view(root.right,arr)

def Boundry_transversal(root):
    arr_left=[]
    arr_leaf=[]
    arr_right=[]
    left_view(root,0,arr_left)
    leaf_view(root,arr_leaf)
    right_view(root,0,arr_right)
    ans=arr_left[:-1]+arr_leaf+arr_right[1:-1][::-1]
    for ele in ans:
        print(ele,end=' ')


tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print("----------Boundry-transversal-------------")
Boundry_transversal(root)

