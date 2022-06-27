import class_level_wise_trasversal
#tale care of left and right direction
class BinaryTreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def tree_using_post_inn(inn,post):
    if len(post)==0:
        return 
    root_val=post[-1]
    root=BinaryTreeNode(root_val)
    ind=-1
    for i in range(len(inn)):
        if inn[i]==root_val:
            ind=i
            break
    left_inn=inn[:ind]
    right_inn=inn[ind+1:]
    left_post=post[:len(left_inn)]
    right_post=post[len(left_inn):-1]
    root.left=tree_using_post_inn(left_inn,left_post)
    root.right=tree_using_post_inn(right_inn,right_post)
    return root
post=[4,5,2,6,7,3,1]
inn=[4,2,5,1,6,3,7]
root=tree_using_post_inn(inn,post)
tree=class_level_wise_trasversal.level_wise_trans()
tree.print_tree_levelwise(root) 