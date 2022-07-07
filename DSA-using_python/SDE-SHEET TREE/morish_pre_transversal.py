import class_level_wise_trasversal

def Pre_order_transversal(root): #my way
    curr=root
    while curr:
        print(curr.data,end=' ')
        if not curr.left:
            curr=curr.right
        else:
            prev=curr.left
            while prev.right and prev.right!=curr.right:
                prev=prev.right
            if not prev.right:
                prev.right=curr.right
                curr=curr.left
            else:
                prev.right=None
                curr=curr.right
    
def Pre_order_transversal_using_iteration(root):   #morris way
    curr=root
    while curr:
        if not(curr.left):
            print(curr.data,end=' ')
            curr=curr.right
        else:
            prev=curr.left
            while prev.right and prev.right!=curr:
                prev=prev.right
            if prev.right==None:
                prev.right=curr
                print(curr.data,end=' ')
                curr=curr.left
            else:
                prev.right=None
                curr=curr.right
tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
Pre_order_transversal(root)