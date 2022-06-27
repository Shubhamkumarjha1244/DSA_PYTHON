import class_level_wise_trasversal

class BinaryTreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None


def Tree_using_in_pre(pre,inn):
    if len(pre)==0:
        return
    root_data=pre[0]
    root=BinaryTreeNode(root_data)
    for ind in range(0,len(inn)):
        if inn[ind]==root_data:
            break
    left_in=inn[:ind]
    right_in=inn[ind+1:]

    left_pre=pre[1:len(left_in)+1]
    right_pre=pre[len(left_in)+1:]
    root.left=Tree_using_in_pre(left_pre,left_in)
    root.right=Tree_using_in_pre(right_pre,right_in)
    return root


#left right ka locha dekh lena hai apna left lena hai screen ka nahi

pre=[1,2,4,5,3,6,7]
inn=[4,2,5,1,6,3,7]
root=Tree_using_in_pre(pre,inn)
tree=class_level_wise_trasversal.level_wise_trans()
tree.print_tree_levelwise(root)





